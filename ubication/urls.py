from rest_framework.urls import path


from ubication.views import (
    ListCountryView,
    CountryByNameView,
    ListProvinceView,
    ProvinceByNameView,
    ProvinceByCountryNameView,
    ListCityView,
    CityByNameView,
    CityByProvinceNameView
)


urlpatterns = [
    path(
        'country/list/',
        ListCountryView.as_view(),
        name='list-country'
    ),
    
    path(
        'country/name/<str:name>',
        CountryByNameView.as_view(),
        name='country-name'
    ),
    
    path(
        'province/list/',
        ListProvinceView.as_view(),
        name='provinces-list'
    ),
    
    path(
        'province/name/<str:name>',
        ProvinceByNameView.as_view(),
        name='province-name'
    ),
    
    path(
        'province/country/<str:country_name>',
        ProvinceByCountryNameView.as_view(),
        name='province-country-name'
    ),
    
    path(
        'city/list/',
        ListCityView.as_view(),
        name='cities-list'
    ),
    
    path(
        'city/name/<str:name>',
        CityByNameView.as_view(),
        name='city-name'
    ),
    
    path(
        'city/province/<str:province_name>',
        CityByProvinceNameView.as_view(),
        name='city-province-name'
    )
]