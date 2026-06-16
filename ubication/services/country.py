from ubication.repositories.country import CountryRepository

class CountryServices:
    @staticmethod
    def get_all_countries():
        return CountryRepository.get_all_country()
    
    @staticmethod
    def get_country_by_name(name):
        return CountryRepository.get_country_by_name(name)