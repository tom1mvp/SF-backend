from django.db import models

from ubication.models import Address

class Genre(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f'Genre: {self.name}'
    
class DocumentType(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f'Document Type: {self.name}'


class Person(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    document_number = models.CharField(max_length=20, null=False)
    phone_number =models.CharField(max_length=20, null=False)
    email = models.EmailField(unique=True, null=False)
    date_birth = models.DateField()
    creation_date = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='people', null=False)
    document_type = models.ForeignKey(DocumentType, on_delete=models.PROTECT, related_name='people', null=False)
    address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='people', null=False)
    
    def __str__(self):
        return f'Person: {self.first_name} - {self.last_name} || Document: {self.document_type.name} - {self.document_number} || Genre: {self.genre.name}'
    
    