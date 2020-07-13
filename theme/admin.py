from django.contrib import admin

from .models import Country, Genre, Band, Album

admin.site.register(Country)
admin.site.register(Genre)
admin.site.register(Band)
admin.site.register(Album)