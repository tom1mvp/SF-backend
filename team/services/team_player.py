from rest_framework.exceptions import ValidationError


from team.repositories.team_player import TeamPlayerRepository


class TeamPlayerServices:
    @staticmethod
    def get_all_team_players():
        return TeamPlayerRepository.get_all_team_player()
    
    @staticmethod
    def get_team_player_by_team_name(name):
        return TeamPlayerRepository.get_team_player_by_team_name(name)
    
    @staticmethod
    def get_team_player_by_team_id(team_id):
        return TeamPlayerRepository.get_team_player_by_team_id(team_id)
    
    @staticmethod
    def get_team_player_by_nickname(nickname):
        return TeamPlayerRepository.get_team_player_by_nickname(nickname)
    
    @staticmethod
    def create_team_player(team_id, player_id, data):
        required_fields = [
            'team_id',
            'player_id'
        ]
        
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'El campo {field} es obligatorio'})
        
        new_team_player = TeamPlayerRepository.create_team_player(team_id, player_id)
        
        return new_team_player
    
    @staticmethod
    def update_team_player(team_id, player_id, team_player_id):
        
        team_player = TeamPlayerRepository.update_team_player(team_player_id, team_id, player_id)
        
        return team_player
    
    @staticmethod
    def delete_team_player(team_player_id):
        team_player = TeamPlayerRepository.delete_team_player(team_player_id)
        
        return team_player