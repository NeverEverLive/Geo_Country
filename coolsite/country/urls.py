from django.urls import path

from .views import *

urlpatterns = [
    path("country/", CountryListView.as_view()),
    path('city/<str:country>/', CityListView.as_view()),
    path('capital/<str:country>/', CapitalListView.as_view()),
]
