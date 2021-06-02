from rest_framework_gis import serializers
from .models import *


class CountryListSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'
        geo_field = 'location'


class CityListSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        model = City
        fields = '__all__'
        geo_field = 'location'


class CapitalListSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        model = Capital
        fields = '__all__'
        geo_field = 'location'
