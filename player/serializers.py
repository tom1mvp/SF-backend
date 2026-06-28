from rest_framework import serializers


from player.models import (
    Player,
    PlayerStats
)

class PlayerListSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    profile_picture = serializers.SerializerMethodField()
    
    class Meta:
        model = Player
        fields = [
            'id',
            'user_id',
            'first_name',
            'last_name',
            'profile_picture',
            'jersey_number',
            'position',
            'preferred_foot',
            'weight',
            'height',
            'nickname'
        ]
    
    def get_user_id(self, obj):
        return obj.user.id
    
    def get_first_name(self, obj):
        return obj.user.person.first_name
    
    def get_last_name(self, obj):
        return obj.user.person.last_name
    
    def get_profile_picture(self, obj):
        picture = getattr(obj.user, 'profile_picture', None)
        return picture.url if picture else None


class PlayStatsListSerializer(serializers.ModelSerializer):
    nickname = serializers.SerializerMethodField()
    player_id = serializers.SerializerMethodField()
    
    class Meta:
        model = PlayerStats
        fields = [
            'id',
            'player_id',
            'nickname',
            'goals',
            'assists',
            'matches_played',
            'yellow_cards',
            'red_cards',
            'total_mvps'
        ]
    
    def get_player_id(self, obj):
        return obj.player.id
    
    def get_nickname(self, obj):
        return obj.player.nickname
    
