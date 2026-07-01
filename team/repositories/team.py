from team.models import Team
from user.models import User


class TeamRepository:
    @staticmethod
    def get_all_teams():
        return Team.objects.all()
    
    @staticmethod
    def get_team_by_name(name):
        return Team.objects.filter(name__icontains=name).first()
    
    @staticmethod
    def get_team_by_id(team_id):
        return Team.objects.filter(id=team_id).first()
    
    @staticmethod
    def create_team(user_id, name, logo):
        user = User.objects.filter(id=user_id).first()
        
        if not user: raise ValueError('User not found')
        
        new_team = Team.objects.create(
            name=name,
            logo=logo,
            user=user
        )
        
        return new_team
    
    @staticmethod
    def update_team(team_id, user_id, name, logo):
        team = Team.objects.filter(id=team_id).first()
        
        if not team: raise ValueError('Team not found')
        
        user = User.objects.filter(id=user_id).first()
        
        if not user: raise ValueError('User not found')
        
        
        team.name = name
        team.logo = logo
        team.user = user
        
        team.save()
        
        return team