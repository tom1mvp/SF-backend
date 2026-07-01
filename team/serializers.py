from rest_framework import serializers


from team.models import (
    Team,
    TeamPlayer,
    TeamStats
)


class TeamListSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    profile_picture = serializers.SerializerMethodField()
    logo = serializers.SerializerMethodField()
    
    class Meta:
        model = Team
        fields = [
            'id',
            'user_id',
            'first_name',
            'last_name',
            'profile_picture',
            'name',
            'logo',
            'created_at',
            'updated_at'
        ]
    def get_user_id(self, obj):
        return obj.user.id
    
    def get_first_name(self, obj):
        return obj.user.person.first_name
    
    def get_last_name(self, obj):
        return obj.user.person.last_name
    
    def get_profile_picture(self, obj):
        picture = getattr(obj.user, 'profile_picture', None)
        return picture.url if picture and hasattr(picture, 'url') and picture else None
    
    def get_logo(self, obj):
        logo = getattr(obj, 'logo', None)
        return logo.url if logo and hasattr(logo, 'url') else None

class TeamPlayerListSerializer(serializers.ModelSerializer):
    nickname = serializers.SerializerMethodField()
    player_id = serializers.SerializerMethodField()
    profile_picture = serializers.SerializerMethodField()
    team_name = serializers.SerializerMethodField()
    team_id = serializers.SerializerMethodField()
    
    class Meta:
        model = TeamPlayer
        fields = [
            'id',
            'player_id',
            'nickname',
            'profile_picture',
            'team_id',
            'team_name'
        ]
    
    def get_player_id(self, obj):
        return obj.player.id
    
    def get_nickname(self, obj):
        return obj.player.nickname
    
    def get_team_id(self, obj):
        return obj.team.id
    
    def get_team_name(self, obj):
        return obj.team.name
    
    def get_profile_picture(self, obj):
        player = getattr(obj, 'player', None)
        user = getattr(player, 'user', None) if player else None
        picture = getattr(user, 'profile_picture', None) if user else None
    
class TeamStatsListSerializer(serializers.ModelSerializer):
    team_name = serializers.SerializerMethodField()
    team_id = serializers.SerializerMethodField()

    class Meta:
        model = TeamStats
        fields = [
            'id',
            'team_id',
            'team_name',
            'matches_played',
            'match_wins',
            'match_ties',
            'match_losses',
            'goals_for',
            'goals_against'
        ]
    def get_team_id(self, obj):
        return obj.team.id

    def get_team_name(self, obj):
        return obj.team.name