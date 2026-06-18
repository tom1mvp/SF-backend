from ubication.models import Address, City


class AddressRepository:
    @staticmethod
    def get_all_addresses():
        return Address.objects.all()
    
    @staticmethod
    def get_address_by_street(street):
        return Address.objects.filter(street_main__icontains=street)
    
    @staticmethod
    def get_address_by_city_name(city_name):
        return Address.objects.filter(city__name__icontains=city_name)
    
    @staticmethod
    def create_address(
        street_main,
        street_complement,
        street_number,
        apartment_number,
        floor,
        comment,
        is_apartment,
        city_id
    ):
        city = City.objects.filter(id=city_id).first()
        
        if not city: raise ValueError('City not found')
        
        new_address = Address.objects.create(
            street_main=street_main,
            street_complement=street_complement,
            street_number=street_number,
            apartment_number=apartment_number,
            floor=floor,
            comment=comment,
            is_apartment=is_apartment,
            city=city
        )
        
        return new_address
    
    @staticmethod
    def update_address(
        address_id,
        street_main,
        street_complement,
        street_number,
        apartment_number,
        floor,
        comment,
        is_apartment,
        city_id
    ):
        address = Address.objects.filter(id=address_id).first()
        
        if not address: raise ValueError('Address not found')


        city = City.objects.filter(id=city_id).first()
        
        if not city: raise ValueError('City not found')
        
        address.street_main=street_main
        address.street_complement=street_complement
        address.street_number=street_number
        address.apartment_number=apartment_number
        address.floor=floor
        address.comment=comment
        address.is_apartment=is_apartment
        address.city=city
        
        address.save()
        return address
