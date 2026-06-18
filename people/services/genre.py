from people.repositories.genre import GenreRepository


from rest_framework.validators import ValidationError


class GenreServices:
    @staticmethod
    def get_all_genres():
        return GenreRepository.get_all_genres()
    
    @staticmethod
    def get_genre_by_name(name):
        return GenreRepository.get_genre_by_name(name)
    