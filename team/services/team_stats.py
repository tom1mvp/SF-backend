from rest_framework.exceptions import ValidationError


from team.repositories.team_stats import TeamStatsRepository


class TeamStatsServices:
    @staticmethod
    def get_all_stats():
        return TeamStatsRepository.get_all_stats()
    
    @staticmethod
    def get_stat_by_team(team_name):
        return TeamStatsRepository.get_team_name(team_name)
    
    @staticmethod
    def get_stat_by_team_id(team_id):
        return TeamStatsRepository.get_stat_by_team_id(team_id)
    
    @staticmethod
    def create_team_stat(data,team_id):
        required_fields = [
            'matches_played',
            'match_wins',
            'match_ties',
            'match_losses',
            'goals_for',
            'goals_against'
        ]
        
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'El campo {field} es obligatorio'})
            
        new_team_stat = TeamStatsRepository.create_team_stat(
            matches_played=data['matches_played'],
            match_wins=data['match_wins'],
            match_ties=data['match_ties'],
            match_losses=data['match_losses'],
            goals_for=data['goals_for'],
            goals_against=data['goals_against'],
            team_id=team_id
        )
        
        return new_team_stat
    
    @staticmethod
    def update_team_stat(data, team_stat_id):
        required_fields = [
            'matches_played',
            'match_wins',
            'match_ties',
            'match_losses',
            'goals_for',
            'goals_against'
        ]
        
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'El campo {field} es obligatorio'})
        
        team_stat = TeamStatsRepository.update_team_stat(
            team_stat_id=team_stat_id,
            matches_played=data['matches_played'],
            match_wins=data['match_wins'],
            match_ties=data['match_ties'],
            match_losses=data['match_losses'],
            goals_for=data['goals_for'],
            goals_against=data['goals_against']
        )
        
        return team_stat
    