from rest_framework.validators import ValidationError


from ubication.repositories.address import AddressRepository


class AddressServices:
    @staticmethod
    def get_all_addresses():
        return AddressRepository.get_all_addresses()
    
    @staticmethod
    def get_address_by_street(street):
        return AddressRepository.get_address_by_street(street)
    
    @staticmethod
    def get_address_by_city_name(city_name):
        return AddressRepository.get_address_by_city_name(city_name)
    
    @staticmethod
    def create_address(
        data,
        city_id
    ):
        
        required_fields = [
            'street_main',
            'street_complement',
            'street_number',
            'comment',
            'is_apartment',
            
        ]
        
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'El campo {field} es obligatorio'})
            
        new_address = AddressRepository.create_address(
            street_main=data['street_main'],
            street_complement=data['street_complement'],
            street_number=data['street_number'],
            apartment_number=data['apartment_number'],
            floor=data['floor'],
            comment=data['comment'],
            is_apartment=data['is_apartment'],
            city_id=city_id
        )
        
        return new_address
    
    @staticmethod
    def update_address(
        address_id,
        data,
        city_id
    ):
        required_fields = [
            'street_main',
            'street_complement',
            'street_number',
            'apartment_number',
            'floor',
            'comment',
            'is_apartment',
        ]
        
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'El campo {field} es obligatorio'})
            
        
        address = AddressRepository.update_address(
            address_id=address_id,
            street_main=data['street_main'],
            street_complement=data['street_complement'],
            street_number=data['street_number'],
            apartment_number=data['apartment_number'],
            floor=data['floor'],
            comment=data['comment'],
            is_apartment=data['is_apartment'],
            city_id=city_id
        )
        
        return address
    