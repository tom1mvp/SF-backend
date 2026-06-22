from django.db import models


from people.models import Person


class Role(models.Model):
    name = models.CharField(max_length=50)
    is_active = True

    def __str__(self):
        return f'Role: {self.name}'

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=120, null=False)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, related_name='users', null=False)
    person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='users', null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'User: {self.user} - Role: {self.role.name}'
