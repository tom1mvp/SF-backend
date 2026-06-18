from rest_framework.validators import ValidationError

from people.repositories.person import PersonRepository


class PersonServices:
    @staticmethod
    def get_all_people():
        return PersonRepository.get_all_people()
    
    @staticmethod
    def get_person_by_name(last_name):
        return PersonRepository.get_person_by_last_name(last_name)
    
    @staticmethod
    def get_person_by_document(document_number):
        return PersonRepository.get_person_by_document(document_number)
    
    @staticmethod
    def create_person(
        data,
        document_type_id,
        genre_id,
        address_id
    ):
        required_fields = [
            'first_name',
            'last_name',
            'document_number',
            'phone_number',
            'email',
            'date_birth',
        ]
        
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'El campo {field} es obligatorio'})
            
            
        new_person = PersonRepository.create_person(
            first_name=data['first_name'],
            last_name=data['last_name'],
            document_number=data['document_number'],
            phone_number=data['phone_number'],
            email=data['email'],
            date_birth=data['date_birth'],
            genre_id=genre_id,
            document_type_id=document_type_id,
            address_id=address_id
        )
        
        return new_person
    
    @staticmethod
    def update_person(
        data,
        person_id,
        document_type_id,
        genre_id,
        address_id
    ):
        required_fields = [
            'first_name',
            'last_name',
            'document_number',
            'phone_number',
            'email',
            'date_birth',
        ]
        
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'El campo {field} es obligatorio'})
            
        person = PersonRepository.update_person(
            person_id=person_id,
            first_name=data['first_name'],
            last_name=data['last_name'],
            document_number=data['document_number'],
            phone_number=data['phone_number'],
            email=data['email'],
            date_birth=data['date_birth'],
            genre_id=genre_id,
            document_type_id=document_type_id,
            address_id=address_id
        )
        
        return person