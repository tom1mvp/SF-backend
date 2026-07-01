from rest_framework.exceptions import ValidationError


from team.repositories.team import TeamRepository


class TeamServices:
    @staticmethod
    def get_all_team():
        return TeamRepository.get_all_teams()
    
    @staticmethod
    def get_team_by_name(name):
        return TeamRepository.get_team_by_name(name)
    
    @staticmethod
    def get_team_by_id(team_id):
        return TeamRepository.get_team_by_id(team_id)
    
    @staticmethod
    def create_team(data, user_id):
        required_fields = [
            'name',
            'logo'
        ]
        
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'El campo {field} es obligatorio'})
            
        new_team = TeamRepository.create_team(
            user_id=user_id,
            name=data['name'],
            logo=data['logo']
        )
        
        return new_team
    
    @staticmethod
    def update_team(team_id, user_id, data):
        required_fields = [
            'name',
            'logo'
        ]
        
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'El campo {field} es obligatorio'})
            
        team = TeamRepository.update_team(
            team_id=team_id,
            user_id=user_id,
            name=data['name'],
            logo=data['logo']
        )
        
        return team
    