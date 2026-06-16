from ubication.models import City


class CityRepository:
    @staticmethod
    def get_all_city():
        return City.objects.all()
    
    @staticmethod
    def get_city_by_name(name):
        return City.objects.filter(name__icontains=name)
    
    @staticmethod
    def get_city_by_province_name(province_name):
        return City.objects.filter(province__name__icontains=province_name)