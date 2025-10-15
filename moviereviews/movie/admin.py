# movie/admin.py
from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_description')
    search_fields = ('title',)

    def short_description(self, obj):
        if obj.description:
            return obj.description[:80] + ('...' if len(obj.description) > 80 else '')
        return ''
    short_description.short_description = 'Description'
