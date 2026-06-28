from django.db import models


from user.models import User


class Player(models.Model):
    jersey_number = models.CharField(max_length=3, null=True, blank=True)
    position = models.CharField(max_length=50)
    preferred_foot = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    nickname = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='players')
    
    def __str__(self):
        return f'Player: {self.user.person.first_name} - {self.user.person.last_name} ({self.nickname}) - Number: {self.jersey_number} - Position: {self.position}'
    
class PlayerStats(models.Model):
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    matches_played = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)
    total_mvps = models.IntegerField(default=0)
    player = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='stats')
    
    def __str__(self):
        return f'Player: {self.player.nickname} - Goals: {self.goals} - Assists: {self.assists} - Yellow cards: {self.yellow_cards} - Red cards: {self.red_cards}'
