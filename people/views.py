from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from people.services.person import PersonServices
from people.services.genre import GenreServices
from people.services.document_type import DocumentTypeServices


from people.serializer import(
    PersonListSerializer,
    GenreListSerializer,
    DocumentTypeListSerializer
)


class ListDocumentTypeView(APIView):
    def get(self, request):
        document_types = DocumentTypeServices.get_all_document_types()
        
        if not document_types:
            return Response({
                "error": "NotFound",
                "message": "Document Types not found"
                
            }, status=status.HTTP_404_NOT_FOUND)
            
        serializer = DocumentTypeListSerializer(document_types, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)


class DocumentTypeByNameView(APIView):
    def get(self, request, *args, **kwargs):
        document_type_name = str(kwargs.get('name'))
        
        if not document_type_name:
            return Response(
                {
                    "error": "ValidationError",
                    "message": "The document type name is required in the URL."
                 
                }, status=status.HTTP_400_BAD_REQUEST)
            
        response = DocumentTypeServices.get_document_type_by_name(document_type_name)
            
        if not response:
            return Response({
            "error": "NotFound",
            "message": "Province not found"
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DocumentTypeListSerializer(response, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    

class ListGenreView(APIView):
    def get(self, request):
        genres = GenreServices.get_all_genres()
        
        if not genres:
            return Response({
                "error": "NotFound",
                "message": "Genres not found"
                
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = GenreListSerializer(genres, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class GenreByNameView(APIView):
    def get(self, request, *args, **kwargs):
        genre_name = str(kwargs.get('name'))
        
        if not genre_name:
            return Response(
                {
                    "error": "ValidationError",
                    "message": "The genre name is required in the URL."
                 
                }, status=status.HTTP_400_BAD_REQUEST)
        
        response = GenreServices.get_genre_by_name(genre_name)
        
        if not response:
            return Response({
                "error": "NotFound",
                "message": "Genre not found"
                
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = GenreListSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    

class ListPeopleView(APIView):
    def get(self, request):
        people = PersonServices.get_all_people()
        
        if not people:
            return Response({
                "error": "NotFound",
                "message": "People not found"
                
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = PersonListSerializer(people, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    

class PersonByLastnameView(APIView):
    def get(self, request, *args, **kwargs):
        last_name = str(kwargs.get('last_name'))
        
        if not last_name:
            return Response(
                {
                    "error": "ValidationError",
                    "message": "The last name is required in the URL."
                 
                }, status=status.HTTP_400_BAD_REQUEST)

        response = PersonServices.get_person_by_name(last_name)
        
        if not response:
            return Response({
                "error": "NotFound",
                "message": "Last name not found"
                
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = PersonListSerializer(response, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    

class PersonByDocumentNumberView(APIView):
    def get(self, request, *args, **kwargs):
        document_number = str(kwargs.get('document_number'))
        
        if not document_number:
            return Response(
                {
                    "error": "ValidationError",
                    "message": "The document number is required in the URL."
                 
                }, status=status.HTTP_400_BAD_REQUEST)
            
        response = PersonServices.get_person_by_document(document_number)
        
        if not response:
            return Response({
                "error": "NotFound",
                "message": "Document number not found"
                
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PersonListSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)


class CreatePersonView(APIView):
    def post(self, request):
        data = request.data
        
        try:
            if not data or not 'genre_id' in data or 'document_type_id' not in data or 'address_id' not in data:
                return Response({"Error": "Sensitive data is missing"}, status=status.HTTP_400_BAD_REQUEST)
        
            response = PersonServices.create_person(
                data,
                data['document_type_id'],
                data['genre_id'],
                data['address_id']
            )
            
            serializer = PersonListSerializer(response)
            
            return Response({
                'message': 'The person has been created successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UpdatePersonView(APIView):
    def put(self, request, *args, **kwargs):
        person_id = int(kwargs.get('id'))
        data = request.data
        
        try:
            if not data or not person_id or 'genre_id' not in data or 'document_type_id' not in data or 'address_id' not in data:
                return Response({"Error": "Sensitive data is missing"}, status=status.HTTP_400_BAD_REQUEST)
            
            response = PersonServices.update_person(
                data,
                person_id,
                data['document_type_id'],
                data['genre_id'],
                data['address_id']
            )
            
            serializer = PersonListSerializer(response)
            
            return Response({
                'Message': 'The person has been successfully updated',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)