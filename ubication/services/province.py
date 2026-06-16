from ubication.repositories.province import ProvinceRepository

class ProvinceServices:
    @staticmethod
    def get_all_provinces():
        return ProvinceRepository.get_all_province()
    
    @staticmethod
    def get_province_by_name(name):
        return ProvinceRepository.get_province_by_name(name)
    
    @staticmethod
    def get_province_by_country_name(country_name):
        return ProvinceRepository.get_province_by_country_name(country_name)
    