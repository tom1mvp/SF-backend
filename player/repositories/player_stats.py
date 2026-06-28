from player.models import Player, PlayerStats


class PlayerStatsRepository:
    @staticmethod
    def get_all_stats():
        return PlayerStats.objects.all()
    
    @staticmethod
    def get_stats_by_player(nickname):
        return PlayerStats.objects.filter(player__nickname__icontains=nickname).first()
    
    @staticmethod
    def get_stats_player(player_id):
        return PlayerStats.objects.filter(id=player_id).first()
    
    @staticmethod
    def create_stats_player(
        goals,
        assists,
        matches_played,
        yellow_cards,
        red_cards,
        total_mvps,
        player_id
    ):
        
        player = Player.objects.filter(id=player_id).first()
        
        if not player: raise ValueError('Player not found')
        
        new_player_stats = PlayerStats.objects.create(
            goals=goals,
            assists=assists,
            matches_played=matches_played,
            yellow_cards=yellow_cards,
            red_cards=red_cards,
            total_mvps=total_mvps,
            player=player
        )
        
        return new_player_stats
    
    @staticmethod
    def update_player_stats(
        player_stats_id,
        goals,
        assists,
        matches_played,
        yellow_cards,
        red_cards,
        total_mvps,
    ):
        player_stats = PlayerStats.objects.filter(id=player_stats_id).first()
        
        if not player_stats: raise ValueError('Player Stats not found')
        
        player_stats.goals=goals
        player_stats.assists=assists
        player_stats.matches_played=matches_played
        player_stats.yellow_cards=yellow_cards
        player_stats.red_cards=red_cards
        player_stats.total_mvps=total_mvps
        
        player_stats.save()
        
        return player_stats