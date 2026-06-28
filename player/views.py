from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from player.services.player import PlayerService
from player.services.player_stats import PlayerStatsService
from player.serializers import PlayerListSerializer, PlayStatsListSerializer


class ListPlayerView(APIView):
    def get(self, request):
        players = PlayerService.get_all_players()
        
        if not players:
            return Response({
                "error": "NotFound",
                "message": "Player not found"
                
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PlayerListSerializer(players, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
class PlayerByUsernameView(APIView):
    def get(self, request, *args, **kwargs):
        username = str(kwargs.get('username'))
        
        if not username:
            return Response(
                {
                    "error": "ValidationError",
                    "message": "The username is required in the URL."
                 
                }, status=status.HTTP_400_BAD_REQUEST)
            
        response = PlayerService.get_player_by_username(username)
        
        if not response:
            return Response({
                "error": "NotFound",
                "message": "Username not found"
                
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PlayerListSerializer(response, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class CreatePlayerView(APIView):
    def post(self, request):
        data = request.data
        
        try:
            if not data or 'user_id' not in data:
                return Response({"Error": "Sensitive data is missing"}, status=status.HTTP_400_BAD_REQUEST)
            
            response = PlayerService.create_player(
                data,
                data['user_id']
            )
            
            serializer = PlayerListSerializer(response)
            return Response({
                'message': 'The player has been created successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class UpdatePlayerView(APIView):
    def put(self, request, *args, **kwargs):
        player_id = int(kwargs.get('id'))
        data = request.data
        
        try:
            if not data or not player_id:
                return Response({"Error": "Sensitive data is missing"}, status=status.HTTP_400_BAD_REQUEST)
            
            response = PlayerService.update_player(
                player_id,
                data
            )
            serializer = PlayerListSerializer(response)
            return Response({
                'message': 'The player has been successfully updated.',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class ListPlayerStatsView(APIView):
    def get(self, request):
        player_stats = PlayerStatsService.get_all_stats()
        
        if not player_stats:
            return Response({
                "error": "NotFound",
                "message": "Player not found"
                
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PlayStatsListSerializer(player_stats, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class PlayerStatsByNicknameView(APIView):
    def get(self, reques, *args, **kwargs):
        nickname = str(kwargs.get('nickname'))
        
        if not nickname:
            return Response(
                {
                    "error": "ValidationError",
                    "message": "The nickname is required in the URL."
                 
                }, status=status.HTTP_400_BAD_REQUEST)
            
        response = PlayerStatsService.get_stats_by_player(nickname)
        
        if not response:
            return Response({
                "error": "NotFound",
                "message": "Nickname not found"
                
            }, status=status.HTTP_404_NOT_FOUND)
            
        serializer = PlayStatsListSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class PlayerStatsByPlayerIDView(APIView):
    def get(self, reques, *args, **kwargs):
        player_id = int(kwargs.get('id'))
        
        if not player_id:
            return Response(
                {
                    "error": "ValidationError",
                    "message": "The player ID is required in the URL."
                 
                }, status=status.HTTP_400_BAD_REQUEST)
        
        response = PlayerStatsService.get_stats_player(player_id)
        
        if not response:
            return Response({
                "error": "NotFound",
                "message": "Player not found"
                
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PlayStatsListSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class CreatePlayerStatsView(APIView):
    def post(self, request):
        data = request.data
        
        try:
            if not data or 'player_id' not in data:
                return Response({"Error": "Sensitive data is missing"}, status=status.HTTP_400_BAD_REQUEST)
            
            response = PlayerStatsService.create_player_stats(
                data,
                data['player_id']
            )
            
            serializer = PlayStatsListSerializer(response)
            
            return Response({
                'message': 'The player stat has been created successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UpdatePlayerStatsView(APIView):
    def put(self, request, *args, **kwargs):
        player_stat_id = int(kwargs.get('id'))
        data = request.data
        
        try:
            if not data or 'player_id' not in data or not player_stat_id:
                return Response({"Error": "Sensitive data is missing"}, status=status.HTTP_400_BAD_REQUEST)
            
            response = PlayerStatsService.update_player_stats(
                data,
                player_stat_id
            )
            
            serializer = PlayStatsListSerializer(response)
            
            return Response({
                'message': 'The player stat has been successfully updated.',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)