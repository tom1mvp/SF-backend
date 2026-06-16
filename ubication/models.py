from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return f'Name: f{self.name}'
    

class Province(models.Model):
    name = models.CharField(max_length=50, null=False)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='provinces', null=False)
    
    def __str__(self):
        return f'Country name: f{self.country.name} - Province name: f{self.name}'
    

class City(models.Model):
    name = models.CharField(max_length=50, null=False)
    province = models.ForeignKey(Province, on_delete=models.PROTECT, related_name='cities', null=False)
    
    def __str__(self):
        return f'Country name: f{self.province.country.name} - Province name: f{self.province.name} - City name: f{self.name}'