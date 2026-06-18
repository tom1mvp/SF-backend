from people.models import Genre


class GenreRepository:
    @staticmethod
    def get_all_genres():
        return Genre.objects.all()
    
    @staticmethod
    def get_genre_by_name(name):
        return Genre.objects.filter(name__icontains=name).first()
    
