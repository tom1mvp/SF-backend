from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from team.services.team import TeamServices
from team.services.team_player import TeamPlayerServices
from team.services.team_stats import TeamStatsServices


from team.serializers import (
    TeamListSerializer,
    TeamPlayerListSerializer,
    TeamStatsListSerializer
)


class ListTeamView(APIView):
    def get(self, request):
        team = TeamServices.get_all_team()
        
        if not team:
            return Response({
                "error": "NotFound",
                "message": "Teams not found"
                
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TeamListSerializer(team, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class TeamByNameView(APIView):
    def get(self, request, *args, **kwargs):
        team_name = str(kwargs.get('name'))
        
        if not team_name:
            return Response(
                {
                    "error": "ValidationError",
                    "message": "The team name is required in the URL."
                 
                }, status=status.HTTP_400_BAD_REQUEST)
        
        response = TeamServices.get_team_by_name(team_name)
        
        if not response:
            return Response({
                "error": "NotFound",
                "message": "Team not found"

            }, status=status.HTTP_404_NOT_FOUND)
            
        serializer = TeamListSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    

class TeamByIdView(APIView):
    def get(self, request, *args, **kwargs):
        team_id = int(kwargs.get('id'))
        
        if not team_id:
            return Response(
                {
                    "error": "ValidationError",
                    "message": "The team ID is required in the URL."
                 
                }, status=status.HTTP_400_BAD_REQUEST)
        
        response = TeamServices.get_team_by_id(team_id)
        
        if not response:
            return Response({
                "error": "NotFound",
                "message": "Team not found"

            }, status=status.HTTP_404_NOT_FOUND)
            
        serializer = TeamListSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class CreateTeamView(APIView):
    def post(self, request):
        data = request.data
        
        try:
            if not data or 'user_id' not in data:
                return Response({"Error": "Sensitive data is missing"}, status=status.HTTP_400_BAD_REQUEST)
            
            response = TeamServices.create_team(data, data['user_id'])
            
            serializer = TeamListSerializer(response)
            return Response({
                'message': 'The team has been created successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class UpdateTeamView(APIView):
    def put(self, request, *args, **kwargs):
        team_id = int(kwargs.get('id'))
        data = request.data
        
        try:
            if not data or 'user_id' not in data or not team_id:
                return Response({"Error": "Sensitive data is missing"}, status=status.HTTP_400_BAD_REQUEST)
            
            response = TeamServices.update_team(
                team_id,
                data['user_id'],
                data
            )
            serializer = TeamListSerializer(response)
            return Response({
                'message': 'The team has been updated successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class ListTeamPlayerView(APIView):
    def get(self, request):
        team_player = TeamPlayerServices.get_all_team_players()
        
        if not team_player:
            return Response({
                "error": "NotFound",
                "message": "Team player not found"
                
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TeamPlayerListSerializer(team_player, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class TeamPlayerByNicknameView(APIView):
    def get(self, request, *args, **kwargs):
        nickname = str(kwargs.get('nickname'))
        
        if not nickname:
            return Response(
                {
                    "error": "ValidationError",
                    "message": "The nickname is required in the URL."
                 
                }, status=status.HTTP_400_BAD_REQUEST)

        response = TeamPlayerServices.get_team_player_by_nickname(nickname)
        
        if not response:
            return Response({
                "error": "NotFound",
                "message": "Player not found"
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TeamPlayerListSerializer(response, many=True)

        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class TeamPlayerByTeamView(APIView):
    def get(self, request, *args, **kwargs):
        team_name = str(kwargs.get('name'))
        
        if not team_name:
            return Response(
                {
                    "error": "ValidationError",
                    "message": "The team name is required in the URL."
                 
                }, status=status.HTTP_400_BAD_REQUEST)
        
        response = TeamPlayerServices.get_team_player_by_team_name(team_name)
        
        if not response:
            return Response({
                "error": "NotFound",
                "message": "Team not found"

            }, status=status.HTTP_404_NOT_FOUND)
            
        serializer = TeamPlayerListSerializer(response, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
    
class TeamPlayerByTeamIdView(APIView):
    def get(self, request, *args, **kwargs):
        team_id = int(kwargs.get('id'))
        
        if not team_id:
            return Response(
                {
                    "error": "ValidationError",
                    "message": "The team ID is required in the URL."
                 
                }, status=status.HTTP_400_BAD_REQUEST)
        
        response = TeamPlayerServices.get_team_player_by_team_id(team_id)
        if not response:
            return Response({
                "error": "NotFound",
                "message": "Team player not found"

            }, status=status.HTTP_404_NOT_FOUND)
            
        serializer = TeamPlayerListSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    

class CreateTeamPlayerView(APIView):
    def post(self, request):
        data = request.data
        
        try:
            if not data or 'team_id' not in data or 'player_id' not in data:
                return Response({"Error": "Sensitive data is missing"}, status=status.HTTP_400_BAD_REQUEST)
            
            response = TeamPlayerServices.create_team_player(data['team_id'], data['player_id'], data)
            
            serializer = TeamPlayerListSerializer(response)
            return Response({
                'message': 'The team player has been created successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UpdateTeamPlayerView(APIView):
    def put(self, request, *args, **kwargs):
        team_player_id = int(kwargs.get('id'))
        data = request.data
        
        try:
            if not data or 'team_id' not in data or 'player_id' not in data or not team_player_id:
                return Response({"Error": "Sensitive data is missing"}, status=status.HTTP_400_BAD_REQUEST)
            
            response = TeamPlayerServices.update_team_player(data['team_id'], data['player_id'], team_player_id)
            
            serializer = TeamPlayerListSerializer(response)
            return Response({
                'message': 'The team player has been updated successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class DeleteTeamPlayerView(APIView):
    def patch(self, request, *args, **kwargs):
        team_player_id = int(kwargs.get('id'))
        
        try:
            TeamPlayerServices.delete_team_player(team_player_id)
            return Response({'message': 'The team player was successfully deactivated.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ListTeamStatView(APIView):
    def get(self, request):
        team_stats = TeamStatsServices.get_all_stats()
        
        if not team_stats:
             return Response({
                "error": "NotFound",
                "message": "Stat not found"
            }, status=status.HTTP_404_NOT_FOUND)
             
        serializer = TeamStatsListSerializer(team_stats, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class TeamStatsByTeamNameView(APIView):
    def get(self, request, *args, **kwargs):
        team_name = str(kwargs.get('name'))
        
        if not team_name:
            return Response(
                {
                    "error": "ValidationError",
                    "message": "The team name is required in the URL."
                 
                }, status=status.HTTP_400_BAD_REQUEST)
        
        response = TeamStatsServices.get_stat_by_team(team_name)
        
        if not response:
            return Response({
                "error": "NotFound",
                "message": "Team not found"

            }, status=status.HTTP_404_NOT_FOUND)

        serializer = TeamStatsListSerializer(response, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    

class TeamStatsByTeamIdView(APIView):
    def get(self, request, *args, **kwargs):
        team_id = int(kwargs.get('id'))
        
        if not team_id:
            return Response(
                {
                    "error": "ValidationError",
                    "message": "The team ID is required in the URL."
                 
                }, status=status.HTTP_400_BAD_REQUEST)
            
        response = TeamStatsServices.get_stat_by_team_id(team_id)
        
        if not response:
            return Response({
                "error": "NotFound",
                "message": "Team  not found"
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TeamStatsListSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class CreateTeamStatView(APIView):
    def post(self, request):
        data = request.data
        
        try:
            if not data or 'team_id' not in data:
                return Response({"Error": "Sensitive data is missing"}, status=status.HTTP_400_BAD_REQUEST)
            
            response = TeamStatsServices.create_team_stat(data, data['team_id'])
            
            serializer = TeamStatsListSerializer(response)
            
            return Response({
                'message': 'The team stat has been created successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class UpdateTeamStatView(APIView):
    def put(self, request, *args, **kwargs):
        team_stat_id = int(kwargs.get('id'))
        data = request.data
        
        try:
            if not data or 'team_id' not in data or not team_stat_id:
                return Response({"Error": "Sensitive data is missing"}, status=status.HTTP_400_BAD_REQUEST)
            
            response = TeamStatsServices.update_team_stat(data, team_stat_id)
            
            serializer = TeamStatsListSerializer(response)
            
            return Response({
                'message': 'The team stat has been updated successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)