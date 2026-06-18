from rest_framework import serializers


from people.models import (
    DocumentType,
    Genre,
    Person
)

class DocumentTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model=DocumentType
        fields='__all__'
        
class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields='__all__'

class PersonListSerializer(serializers.ModelSerializer):
    genre_name = serializers.SerializerMethodField()
    document_type_name = serializers.SerializerMethodField()
    address_street = serializers.SerializerMethodField()
    address_street_number = serializers.SerializerMethodField()
    
    class Meta:
        model=Person
        fields=[
            'id',
            'first_name',
            'last_name',
            'document_number',
            'document_type_name',
            'phone_number',
            'email',
            'genre_name',
            'address_street',
            'address_street_number',
            'date_birth',
            'creation_date',
        ]
    
    def get_genre_name(self, obj):
        return obj.genre.name
    
    def get_document_type_name(self, obj):
        return obj.document_type.name
    
    def get_address_street(self, obj):
        return obj.address.street_main
    
    def get_address_street_number(self, obj):
        return obj.address.street_number