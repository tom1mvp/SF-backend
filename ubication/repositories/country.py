from ubication.models import Country


class CountryRepository:
    @staticmethod
    def get_all_country():
        return Country.objects.all()
    
    @staticmethod
    def get_country_by_name(name):
       return  Country.objects.filter(name__icontains=name)
