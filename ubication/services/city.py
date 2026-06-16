from ubication.repositories.city import CityRepository


class CityServices:
    @staticmethod
    def get_all_cities():
        return CityRepository.get_all_city()
    
    @staticmethod
    def get_city_by_name(name):
        return CityRepository.get_city_by_name(name)
    
    @staticmethod
    def get_city_by_province_name(province_name):
        return CityRepository.get_city_by_province_name(province_name)