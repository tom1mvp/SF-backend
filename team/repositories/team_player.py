from team.models import Team, TeamPlayer
from player.models import Player


class TeamPlayerRepository:
    @staticmethod
    def get_all_team_player():
        return TeamPlayer.objects.all()
    
    @staticmethod
    def get_team_player_by_team_name(name):
        return TeamPlayer.objects.filter(team__name__icontains=name)
    
    @staticmethod
    def get_team_player_by_team_id(team_id):
        return TeamPlayer.objects.filter(team_id=team_id).first()
    
    @staticmethod
    def get_team_player_by_nickname(nickname):
        return TeamPlayer.objects.filter(player__nickname__icontains=nickname)
    
    @staticmethod
    def create_team_player(team_id, player_id, is_active=True):
        team = Team.objects.filter(id=team_id).first()
        
        if not team: raise ValueError('Team not found')
        
        player = Player.objects.filter(id=player_id).first()
        
        if not player: raise ValueError('Player not found')
        
        new_team_player = TeamPlayer.objects.create(
            team=team,
            player=player,
            is_active=is_active
        )
        
        return new_team_player
    
    @staticmethod
    def update_team_player(team_player_id, team_id, player_id):
        team_player = TeamPlayer.objects.filter(id=team_player_id).first()
        
        if not team_player: raise ValueError('Team player not found')
        
        team = Team.objects.filter(id=team_id).first()
        
        if not team: raise ValueError('Team not found')
        
        player = Player.objects.filter(id=player_id).first()
        
        if not player: raise ValueError('Player not found')
        
        team_player.team=team
        team_player.player=player
        
        team_player.save()
        
        return team_player
    
    @staticmethod
    def delete_team_player(team_player_id):
        team_player = TeamPlayer.objects.filter(id=team_player_id).first()

        if not team_player: raise ValueError('Team player not found')
        
        if team_player.is_active:
            team_player.is_active = False
            
            team_player.save()
            
            return team_player