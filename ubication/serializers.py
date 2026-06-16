from rest_framework import serializers

from ubication.models import (
    Country,
    Province,
    City
)

class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields='__all__'
    
class ProvinceListSerializer(serializers.ModelSerializer):
    country_id = serializers.SerializerMethodField()
    country_name = serializers.SerializerMethodField()
    
    class Meta:
        model=Province
        fields = [
            'id',
            'name',
            'country_id',
            'country_name'
        ]
    
    
    def get_country_id(self, obj):
        return obj.country.id

    def get_country_name(self, obj):
        return obj.country.name

class CityListSerializer(serializers.ModelSerializer):
    country_id = serializers.SerializerMethodField()
    country_name = serializers.SerializerMethodField()
    province_id = serializers.SerializerMethodField()
    province_name = serializers.SerializerMethodField()
    
    class Meta:
        model=City
        fields = [
            'id',
            'name',
            'country_id',
            'country_name',
            'province_id',
            'province_name'
        ]
        

    def get_province_id(self, obj):
        return obj.province.id

    def get_province_name(self, obj):
        return obj.province.name
    
    def get_country_id(self, obj):
        return obj.province.country.id

    def get_country_name(self, obj):
        return obj.province.country.name