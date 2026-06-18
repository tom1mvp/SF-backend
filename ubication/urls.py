from rest_framework.urls import path


from ubication.views import (
    ListCountryView,
    CountryByNameView,
    ListProvinceView,
    ProvinceByNameView,
    ProvinceByCountryNameView,
    ListCityView,
    CityByNameView,
    CityByProvinceNameView,
    ListAddressesView,
    AddressByStreetView,
    AddressByCityNameView,
    CreateAddressView,
    UpdateAddressView
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
    ),
    
    path(
        'address/list/',
        ListAddressesView.as_view(),
        name='addresses-list'
    ),
    path(
        'address/street/<str:street>',
        AddressByStreetView.as_view(),
        name='address-by-street'
    ),
    path(
        'address/city/<str:city_name>',
        AddressByCityNameView.as_view(),
        name='street-by-city'
    ),
    path(
        'address/create/',
        CreateAddressView.as_view(),
        name='create-address'
    ),
    
    path(
        'address/update/<int:id>',
        UpdateAddressView.as_view(),
        name='update-address'
    )
]