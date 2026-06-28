from player.repositories.player_stats import PlayerStatsRepository


from rest_framework.exceptions import ValidationError


class PlayerStatsService:
    @staticmethod
    def get_all_stats():
        return PlayerStatsRepository.get_all_stats()
    
    @staticmethod
    def get_stats_by_player(nickname):
        return PlayerStatsRepository.get_stats_by_player(nickname)
    
    @staticmethod
    def get_stats_player(player_id):
        return PlayerStatsRepository.get_stats_player(player_id)
    
    @staticmethod
    def create_player_stats(
        data,
        player_id
    ):
        required_fields = [
            'goals',
            'assists',
            'matches_played',
            'yellow_cards',
            'red_cards',
            'total_mvps',
        ]
        
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'El campo {field} es obligatorio'})
            
        new_player_stats = PlayerStatsRepository.create_stats_player(
            goals=data['goals'],
            assists=data['assists'],
            matches_played=data['matches_played'],
            yellow_cards=data['yellow_cards'],
            red_cards=data['red_cards'],
            total_mvps=data['total_mvps'],
            player_id=player_id
        )
        
        return new_player_stats
    
    @staticmethod
    def update_player_stats(
        data,
        player_stats_id
    ):
        required_fields = [
            'goals',
            'assists',
            'matches_played',
            'yellow_cards',
            'red_cards',
            'total_mvps',
        ]
        
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'El campo {field} es obligatorio'})
            
        player_stats = PlayerStatsRepository.update_player_stats(
            player_stats_id=player_stats_id,
            goals=data['goals'],
            assists=data['assists'],
            matches_played=data['matches_played'],
            yellow_cards=data['yellow_cards'],
            red_cards=data['red_cards'],
            total_mvps=data['total_mvps'],
        )
        
        return player_stats