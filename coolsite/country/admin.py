from django.contrib import admin
from .models import Country, City, Capital


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location',)
    list_display_links = ('name', )
    search_fields = ('name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country',)
    list_display_links = ('name', )
    search_fields = ('name',)


@admin.register(Capital)
class CapitalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')
    list_display_links = ('name', )
    search_fields = ('name',)

# admin.site.register(Country, CountryAdmin)
# admin.site.register(City)
# admin.site.register(Capital)

# Register your models here.
