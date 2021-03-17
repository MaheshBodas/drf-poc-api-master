from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions

from chinookapi.models import Artist, Album, MediaType, Genre, Track
from chinookapi.serializers import UserSerializer, TrackSerializer
from django_filters import rest_framework as filters


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('username', 'email', 'is_staff',)
    permission_classes = (permissions.IsAuthenticated,)


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'name', 'album', 'media_type', 'genre')
    serializer_class = TrackSerializer
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['get']

    def pre_save(self, obj):
        obj.createdby = self.request.user