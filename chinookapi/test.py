from enum import Enum
from django.contrib.auth.models import User
from chinookapi.models import Artist, Album, MediaType, Genre, Track
from chinookapi.serializers import UserSerializer, TrackSerializer
from chinookapi.views import *
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
import json


TrackArray = [dict(id=1, album=1, album_title="For Those About To Rock We Salute You",
                   name="For Those About To Rock (We Salute You)", media_type=1, media_name="MPEG audio file", genre=1,
                   genre_name="Rock", composer="Angus Young, Malcolm Young, Brian Johnson", milliseconds=343719,
                   bytes=11170334, unit_price="0.99")]

class SetupUser(Enum):
    ADMIN = 1
    NONADMIN = 2


class SetUserHelper(object):
    def __init__(self, setupUser):
        self.setupUser = setupUser

    def getUserPassword(self):
        if self.setupUser is SetupUser.ADMIN:
            return 'mahesh.bodas', "mypassword"
        elif self.setupUser is SetupUser.NONADMIN:
            return 'editor', "urpassword"

    def getUserPasswordEmail(self):
        if self.setupUser is SetupUser.ADMIN:
            return 'mahesh.bodas', "mypassword", 'myemail@test.com'
        elif self.setupUser is SetupUser.NONADMIN:
            return 'editor', "urpassword", 'myeditor@test.com'


#

class TestTrack(APITestCase):
    def setUp(self):
        self.userHelper = SetUserHelper(SetupUser.ADMIN)

        username, password, email = self.userHelper.getUserPasswordEmail()
        User.objects.create_user(
            username, email, password)
        self.user1 = User.objects.create_user(username="admin")

        self.client = APIClient()
        self.client.login(username=username, password=password)

        self.artist = Artist.objects.create(name='Pink Floyd')
        self.album = Album.objects.create(artist=self.artist,
                                          title='For Those About To Rock We Salute You')
        self.genre = Genre.objects.create(name='Rock')
        self.media_type = MediaType.objects.create(name='MPEG audio file')

        self.track = Track.objects.create(album=self.album,
                                          media_type=self.media_type,
                                          genre=self.genre,
                                          name='For Those About To Rock (We Salute You)',
                                          composer='Angus Young, Malcolm Young, Brian Johnson',
                                          milliseconds=343719,
                                          bytes=11170334,
                                          unit_price=0.99
                                          )

    def test_PostRequest(self):
        # return PostRequest_RisksDict[self.getPayloadKey()]
        username, password = self.userHelper.getUserPassword()
        self.client.login(username=username, password=password)
        # response = self.client.get('/tracks/?risk_type_name=Automobile',
        response = self.client.get('/tracks/', format='json')
        # response = self.view(request)
        # print(json.dumps(response.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertTrue(response, TrackArray)
