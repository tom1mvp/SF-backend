from player.repositories.player import PlayerRepository


from rest_framework.exceptions import ValidationError


class PlayerService:
    @staticmethod
    def get_all_players():
        return PlayerRepository.get_all_players()
    
    @staticmethod
    def get_player_by_username(username):
        return PlayerRepository.get_player_by_username(username)
    
    @staticmethod
    def create_player(data, user_id):
        required_fields = [
            'jersey_number',
            'position',
            'preferred_foot',
            'weight',
            'height',
            'nickname'
        ]
        
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'El campo {field} es obligatorio'})
            
        new_player = PlayerRepository.create_player(
            jersey_number=data['jersey_number'],
            position=data['position'],
            preferred_foot=data['preferred_foot'],
            weight=data['weight'],
            height=data['height'],
            nickname=data['nickname'],
            user_id=user_id
        )
        
        return new_player
    
    @staticmethod
    def update_player(
        player_id,
        data,
    ):
        required_fields = [
            'jersey_number',
            'position',
            'preferred_foot',
            'weight',
            'height',
            'nickname'
        ]
        
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'El campo {field} es obligatorio'})
            
        player = PlayerRepository.update_player(
            player_id=player_id,
            jersey_number=data['jersey_number'],
            position=data['position'],
            preferred_foot=data['preferred_foot'],
            weight=data['weight'],
            height=data['height'],
            nickname=data['nickname'],
        )
        
        return player