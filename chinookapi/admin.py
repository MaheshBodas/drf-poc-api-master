from django.contrib import admin
from chinookapi.models import Artist, Album, MediaType, Genre, Track

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(MediaType)
admin.site.register(Genre)
admin.site.register(Track)