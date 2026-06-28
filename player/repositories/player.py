from player.models import Player
from user.models import User


class PlayerRepository:
    @staticmethod
    def get_all_players():
        return Player.objects.all()
    
    @staticmethod
    def get_player_by_username(username):
        return Player.objects.filter(user__username__icontains=username)
    
    @staticmethod
    def create_player(
        jersey_number,
        position,
        preferred_foot,
        weight,
        height,
        nickname,
        user_id
    ):
        user = User.objects.filter(id=user_id).first()
        
        if not user: raise ValueError('User not found')
        
        new_player = Player.objects.create(
            jersey_number=jersey_number,
            position=position,
            preferred_foot=preferred_foot,
            weight=weight,
            height=height,
            nickname=nickname,
            user=user
        )
        
        return new_player
    
    @staticmethod
    def update_player(
        player_id,
        jersey_number,
        position,
        preferred_foot,
        weight,
        height,
        nickname
    ):
        player = Player.objects.filter(id=player_id).first()
        
        if not player: raise ValueError('Player not found')
        
        
        player.jersey_number=jersey_number
        player.position=position
        player.preferred_foot=preferred_foot
        player.weight=weight
        player.height=height
        player.nickname=nickname
        
        player.save()
        
        return player