from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from ubication.services.city import CityServices
from ubication.services.province import ProvinceServices
from ubication.services.country import CountryServices
from ubication.services.address import AddressServices


from ubication.serializers import (
    CityListSerializer,
    ProvinceListSerializer,
    CountryListSerializer,
    AddressListSerializer
)


# View's Country
class ListCountryView(APIView):
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
    
class ListAddressesView(APIView):
    def get(self, request):
        addresses = AddressServices.get_all_addresses()
        
        if not addresses:
            return Response({
                "error": "NotFound",
                "message": "Address not found"
                
            }, status=status.HTTP_404_NOT_FOUND)
            
        serializer = AddressListSerializer(addresses, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class AddressByStreetView(APIView):
    def get(self, request, *args, **kwargs):
        street = str(kwargs.get('street'))
        
        if not street:
            return Response(
                {
                    "error": "ValidationError",
                    "message": "The street name is required in the URL."
                 
                }, status=status.HTTP_400_BAD_REQUEST)
        
        response = AddressServices.get_address_by_street(street)
        
        if not response:
            return Response({
                "error": "NotFound",
                "message": "Street not found"
                
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AddressListSerializer(response, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class AddressByCityNameView(APIView):
    def get(self, request, *args, **kwargs):
        city_name = str(kwargs.get('city_name'))
        
        if not city_name:
            return Response(
                {
                    "error": "ValidationError",
                    "message": "The city name is required in the URL."
                 
                }, status=status.HTTP_400_BAD_REQUEST)
        
        response = AddressServices.get_address_by_city_name(city_name)
        
        if not response:
            return Response({
                "error": "NotFound",
                "message": "City not found"

            }, status=status.HTTP_404_NOT_FOUND)

        serializer = AddressListSerializer(response, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class CreateAddressView(APIView):
    def post(self, request):
        data = request.data

        try:
            if not data or 'city_id' not in data:
                return Response({"Error": "Sensitive data is missing"}, status=status.HTTP_400_BAD_REQUEST)

            response = AddressServices.create_address(
                data,
                data['city_id']
            )

            serializer = AddressListSerializer(response)

            return Response({
                'message': 'The address has been created successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UpdateAddressView(APIView):
    def put(self, request, *args, **kwargs):
        address_id = int(kwargs.get('id'))
        data = request.data

        try:
            if not data or 'city_id' not in data or not address_id:
                return Response({"Error": "Sensitive data is missing"}, status=status.HTTP_400_BAD_REQUEST)

            response = AddressServices.update_address(
                address_id,
                data,
                data['city_id']
            )

            serializer = AddressListSerializer(response)

            return Response({
                'Message': 'The address has been successfully updated',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)