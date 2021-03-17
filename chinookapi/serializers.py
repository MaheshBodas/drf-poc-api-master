from django.contrib.auth.models import User
from rest_framework import serializers
from chinookapi.models import Artist, Album, MediaType, Genre, Track


# Serializer type for User DRF authentication


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'username', 'email', 'is_staff',
                  'is_superuser', 'is_active', 'date_joined',)
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser',
                            'is_active', 'date_joined',)
        # Explicitly mark required fields
        required_fields = (
            'username',
            'password'
        )
        extra_kwargs = {field: {'required': True} for field in required_fields}


# Serializer type used for Lookups in select Track list in UI
class TrackKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'name')

# Serializer type used for Lookups in select risk list in UI


class TrackSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):
    createdby = serializers.ReadOnlyField(source='createdby.username')
    album_title = serializers.ReadOnlyField(source='album.title')
    media_name = serializers.ReadOnlyField(source='media_type.name')
    genre_name = serializers.ReadOnlyField(source='genre.name')

    class Meta:
        model = Track
        fields = ('id', 'album', 'album_title', 'name',
                  'media_type', 'media_name',
                  'genre', 'genre_name', 'composer', 'milliseconds', 'bytes', 'unit_price',
                  'createdby')
        # Explicitly mark required fields
        required_fields = (
            'album',
            'media_type',
            'genre'
        )
        extra_kwargs = {field: {'required': True} for field in required_fields}

