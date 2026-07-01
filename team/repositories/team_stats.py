from team.models import TeamStats, Team


class TeamStatsRepository:
    @staticmethod
    def get_all_stats():
        return TeamStats.objects.all()
    
    @staticmethod
    def get_stat_by_team_id(team_id):
        return TeamStats.objects.filter(team_id=team_id).first()
    
    
    @staticmethod
    def get_team_name(team_name):
        return TeamStats.objects.filter(team__name__icontains=team_name)
    
    @staticmethod
    def create_team_stat(
        matches_played,
        match_wins,
        match_ties,
        match_losses,
        goals_for,
        goals_against,
        team_id
    ):
        team = Team.objects.filter(id=team_id).first()
        
        if not team: raise ValueError('Team stat not found')
        
        new_team_stat = TeamStats.objects.create(
            matches_played=matches_played,
            match_wins=match_wins,
            match_ties=match_ties,
            match_losses=match_losses,
            goals_for=goals_for,
            goals_against=goals_against,
            team=team
        )
        
        return new_team_stat
    
    @staticmethod
    def update_team_stat(
        team_stat_id,
        matches_played,
        match_wins,
        match_ties,
        match_losses,
        goals_for,
        goals_against,
    ):
        team_stat = TeamStats.objects.filter(id=team_stat_id).first()
        
        if not team_stat: raise ValueError('Stat not found')
        
        team_stat.matches_played=matches_played
        team_stat.match_wins=match_wins
        team_stat.match_ties=match_ties
        team_stat.match_losses=match_losses
        team_stat.goals_for=goals_for
        team_stat.goals_against=goals_against
        
        team_stat.save()
        
        return team_stat