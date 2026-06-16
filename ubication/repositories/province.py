from ubication.models import Province


class ProvinceRepository:
    @staticmethod
    def get_all_province():
        return Province.objects.all()
    
    @staticmethod
    def get_province_by_name(name):
        return Province.objects.filter(name__icontains=name)
    
    @staticmethod
    def get_province_by_country_name(country_name):
        return Province.objects.filter(country__name__icontains=country_name)