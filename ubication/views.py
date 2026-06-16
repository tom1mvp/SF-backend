from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser


from ubication.services.city import CityServices
from ubication.services.province import ProvinceServices
from ubication.services.country import CountryServices


from ubication.serializers import (
    CityListSerializer,
    ProvinceListSerializer,
    CountryListSerializer
)


# View's Country
class ListCountryView(APIView):
    
    # permission_classes = [IsAdminUser]
    
    def get(self, request):
        
        country = CountryServices.get_all_countries()
        
        if not country:
            return Response({
                "error": "NotFound",
                "message": "Country not found"
                
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CountryListSerializer(country, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class CountryByNameView(APIView):
    
    # permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        country_name = str(kwargs.get('name'))
        
        if not country_name:
            return Response(
                {
                    "error": "ValidationError",
                    "message": "The country name is required in the URL."
                 
                }, status=status.HTTP_400_BAD_REQUEST)

        response = CountryServices.get_country_by_name(country_name)
        
        if not response:
            return Response({
                "error": "NotFound",
                "message": "Province not found"
            },  status=status.HTTP_404_NOT_FOUND)
        
        serializer = CountryListSerializer(response, many=True)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    

class ListProvinceView(APIView):
    
    # permission_classes = [IsAdminUser]
    
    def get(self, request):
        provinces = ProvinceServices.get_all_provinces()
        
        if not provinces:
            return Response({
                "error": "NotFound",
                "message": "Province not found"
                
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProvinceListSerializer(provinces, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    

class ProvinceByNameView(APIView):
    
    # permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        province_name = str(kwargs.get('name'))
        
        if not province_name:
            return Response(
                {
                    "error": "ValidationError",
                    "message": "The province name is required in the URL."
                 
                }, status=status.HTTP_400_BAD_REQUEST)
        
        response = ProvinceServices.get_province_by_name(province_name)
        
        if not response:
            return Response({
                "error": "NotFound",
                "message": "Province not found"
                
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProvinceListSerializer(response, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    

class ProvinceByCountryNameView(APIView):
    
    # permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        country_name = str(kwargs.get('country_name'))
        
        if not country_name:
            return Response(
                {
                    "error": "ValidationError",
                    "message": "The country name is required in the URL."
                 
                }, status=status.HTTP_400_BAD_REQUEST)
            
        response = ProvinceServices.get_province_by_country_name(country_name)
        
        if not response:
            return Response({
                "error": "NotFound",
                "message": "Country not found"
                
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProvinceListSerializer(response, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    

class ListCityView(APIView):
    
    # permission_classes = [IsAdminUser]
    
    def get(self, request):
        cities = CityServices.get_all_cities()
        
        if not cities:
            return Response({
                "error": "NotFound",
                "message": "City not found"
                
            }, status=status.HTTP_404_NOT_FOUND)
            
        serializer = CityListSerializer(cities, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
    
class CityByNameView(APIView):
    
    # permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        city_name = str(kwargs.get('name'))
        
        if not city_name:
            return Response(
                {
                    "error": "ValidationError",
                    "message": "The city name is required in the URL."
                 
                }, status=status.HTTP_400_BAD_REQUEST)
            
        response = CityServices.get_city_by_name(city_name)
        
        if not response:
            return Response({
                "error": "NotFound",
                "message": "City not found"
                
            }, status=status.HTTP_404_NOT_FOUND)
            
        serializer = CityListSerializer(response, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    

class CityByProvinceNameView(APIView):
    
    # permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        province_name = str(kwargs.get('province_name'))
        
        if not province_name:
            return Response(
                {
                    "error": "ValidationError",
                    "message": "The province name is required in the URL."
                 
                }, status=status.HTTP_400_BAD_REQUEST)
            
        response = CityServices.get_city_by_province_name(province_name)
        
        if not response:
             return Response({
                "error": "NotFound",
                "message": "Province not found"
                
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CityListSerializer(response, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)