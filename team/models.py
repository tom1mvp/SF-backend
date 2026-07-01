from django.db import models


from player.models import Player
from user.models import User


class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='teams')
    logo = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def _str_(self):
        return f'Team: {self.name} - Owner: {self.user.username}'


class TeamPlayer(models.Model):
    is_active = models.BooleanField(default=True)
    player = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='team_players')
    team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='team_players')

    def _str_(self):
        return f'Player: {self.player.nickname} - Team: {self.team.name}'

class TeamStats(models.Model):
    matches_played = models.IntegerField(default=0)
    match_wins = models.IntegerField(default=0)
    match_ties = models.IntegerField(default=0)
    match_losses = models.IntegerField(default=0)
    goals_for = models.IntegerField(default=0)
    goals_against = models.IntegerField(default=0)
    team = models.OneToOneField(Team, on_delete=models.PROTECT, related_name='stats')

    def _str_(self):
        return f'Stats for {self.team.name} - MP: {self.matches_played} - W: {self.match_wins} - T: {self.match_ties} - L: {self.match_losses}'

