from django.contrib import admin

from .models import Location

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_available', 'price', 'added_date', 'cleaner')
    list_display_links = ('id', 'title')
    list_filter = ('cleaner',)
    list_editable = ('is_available',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25

admin.site.register(Location, LocationAdmin)
