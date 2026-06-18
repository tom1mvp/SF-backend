from people.models import Person, DocumentType, Genre
from ubication.models import Address


class PersonRepository:
    @staticmethod
    def get_all_people():
        return Person.objects.all()
    
    @staticmethod
    def get_person_by_last_name(last_name):
        return Person.objects.filter(last_name__icontains=last_name)
    
    @staticmethod
    def get_person_by_document(document_number):
        return Person.objects.filter(document_number=document_number).first()
    
    @staticmethod
    def create_person(
        first_name,
        last_name,
        document_number,
        phone_number,
        email,
        date_birth,
        genre_id,
        document_type_id,
        address_id
    ):
        document_type = DocumentType.objects.filter(id=document_type_id).first()
        
        if not document_type: raise ValueError('Document type not found')
        
        genre = Genre.objects.filter(id=genre_id).first()
        
        if not genre: raise ValueError('Genre not found')
        
        address = Address.objects.filter(id=address_id).first()
        
        if not address: raise ValueError('Address not found')
        
        new_person = Person.objects.create(
            first_name=first_name,
            last_name=last_name,
            document_number=document_number,
            phone_number=phone_number,
            email=email,
            date_birth=date_birth,
            genre=genre,
            document_type=document_type,
            address=address
        )
        
        return new_person
    
    @staticmethod
    def update_person(
        person_id,
        first_name,
        last_name,
        document_number,
        phone_number,
        email,
        date_birth,
        genre_id,
        document_type_id,
        address_id
    ):
        person = Person.objects.filter(id=person_id).first()
        
        if not person: raise ValueError('Person not found')
        
        document_type = DocumentType.objects.filter(id=document_type_id).first()
        
        if not document_type: raise ValueError('Document type not found')
        
        genre = Genre.objects.filter(id=genre_id).first()
        
        if not genre: raise ValueError('Genre not found')
        
        address = Address.objects.filter(id=address_id).first()
        
        if not address: raise ValueError('Address not found')
        
        person.first_name = first_name
        person.last_name = last_name
        person.document_number = document_number
        person.phone_number = phone_number
        person.email = email
        person.date_birth = date_birth
        person.genre = genre
        person.document_type = document_type
        
        person.save()
        
        return person