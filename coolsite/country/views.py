from rest_framework.views import APIView
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework_gis.pagination import GeoJsonPagination

# from .models import *
from .serializers import *


class CountryListView(generics.ListAPIView):
    """Вывод списка стран"""
    serializer_class = CountryListSerializer
    queryset = Country.objects.all()
    pagination_class = GeoJsonPagination


class CityListView(APIView):
    """Вывод списка городов"""
    serializer_class = CityListSerializer
    queryset = City.objects.all()
    pagination_class = GeoJsonPagination

    def get(self, request, country):
        paginator = GeoJsonPagination()
        paginator.page_size = 3
        model = City.objects.filter(country = country)
        result = paginator.paginate_queryset(model, request)
        serializer = CityListSerializer(result, many=True)
        return paginator.get_paginated_response(serializer.data)


class CapitalListView(APIView):
    """Вывод списка столиц"""
    serializer_class = CapitalListSerializer
    queryset = Capital.objects.all()
    pagination_class = GeoJsonPagination

    def get(self, request, country):
        paginator = GeoJsonPagination()
        paginator.page_size = 3
        model = Capital.objects.filter(country = country)
        result = paginator.paginate_queryset(model, request)
        serializer = CapitalListSerializer(result, many=True)
        return paginator.get_paginated_response(serializer.data)
