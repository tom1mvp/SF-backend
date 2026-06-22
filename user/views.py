import secrets


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken


from user.services.user import UserServices
from emails.services import EmailServices


from user.serializer import (
    UserListSerializer
)

class ListUserView(APIView):
    def get(self, request):
        users = UserServices.get_all_users()
        
        if not users:
            return Response({
                "error": "NotFound",
                "message": "Users not found"
                
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserListSerializer(users, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class UserByUsernameView(APIView):
    def get(self, request, *args, **kwargs):
        username = str(kwargs.get('username'))
        
        if not username:
            return Response(
                {
                    "error": "ValidationError",
                    "message": "The username is required in the URL."
                 
                }, status=status.HTTP_400_BAD_REQUEST)
        
        response = UserServices.get_user_by_username(username)
        
        if not response:
            return Response({
                "error": "NotFound",
                "message": "Username not found"
                
            }, status=status.HTTP_404_NOT_FOUND)
            
        serializer = UserListSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class UserByEmailView(APIView):
    def get(self, request, *args, **kwargs):
        email = str(kwargs.get('email'))
        
        if not email:
            return Response(
                {
                    "error": "ValidationError",
                    "message": "The email is required in the URL."
                 
                }, status=status.HTTP_400_BAD_REQUEST)
        
        response = UserServices.get_user_by_email(email)
        
        if not response:
            return Response({
                "error": "NotFound",
                "message": "Email not found"
                
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserListSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    

class LoginView(APIView):
    def post(self, request):
        data = request.data
        
        if 'username' not in data or 'password' not in data:
            return Response(
                {
                    "Error": "Sensitive data is missing"
                }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            response = UserServices.login(data)
            
            token = RefreshToken.for_user(response)
            
            serializer = UserListSerializer(response)
            return Response({'Message': 'Welcome, user', "data": serializer.data, "token": str(token.access_token)}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        
        try:
            response = UserServices.register(
                data,
                data['role_id'],
                data['person_id']
            )
            
            token = RefreshToken.for_user(response)
            
            serializer = UserListSerializer(response)
            
            return Response({
                'message': 'Successfully registered user',
                'data': serializer.data,
                "token": str(token.access_token)
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class UpdateUserView(APIView):
    def put(self, request, *args, **kwargs):
        data = request.data
        user_id = int(kwargs.get('id'))
        
        try:
            response = UserServices.update_user(data, user_id)
            serializer = UserListSerializer(response)
            
            return Response({
                'Message': 'The user has been successfully updated',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class DeleteUserView(APIView):
    def patch(self, request, *args, **kwargs):
        user_id = int(kwargs.get('id'))
        try:
            UserServices.delete_user(user_id)
            return Response({'message': 'The user was successfully deactivated.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class RecoverUserView(APIView):
    def patch(self, request, *args, **kwargs):
        email = str(kwargs.get('email'))
        
        try:
            UserServices.recover_user(email)
            return Response({'message': 'The user was successfully recovered.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class RecoverPasswordView(APIView):
    def patch(self, request, *args, **kwargs):
        user_id = int(kwargs.get('id'))
        data = request.data
        
        if not data:
            return Response({"Error": "Sensitive data is missing"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            UserServices.recover_password(
                user_id,
                data
            )
            return Response({'message': 'The password was successfully recovered.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class SendEmailPasswordResetView(APIView):
    def post(self, request, *args, **kwargs):
        email = str(kwargs.get('email'))
        username = str(kwargs.get('username'))
        
        if not email or not username:
            return Response(
                {
                    "error": "BadRequest",
                    "message": "Sensitive data is missing"
                }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            
            token = secrets.token_hex(20)
            
            response = EmailServices.send_password_reset_email(email, username, token)
        
            if not response:
                return Response({
                    "error": "BadResquest",
                    "message": "We were unable to send the recovery email"
                
                }, status=status.HTTP_400_BAD_REQUEST)
        
            return Response({'message': 'The email recover was successfully sender.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        
class SendEmailReactivationUserView(APIView):
    def post(self, request, *args, **kwargs):
        email = str(kwargs.get('email'))
        username = str(kwargs.get('username'))
        
        if not email or not username:
            return Response(
                {
                    "error": "BadRequest",
                    "message": "Sensitive data is missing"
                }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            
            token = secrets.token_hex(20)
            
            response = EmailServices.send_reactivation_link_email(email, username, token)
        
            if not response:
                return Response({
                    "error": "BadResquest",
                    "message": "We were unable to send the recovery email"
                
                }, status=status.HTTP_400_BAD_REQUEST)
        
            return Response({'message': 'The email recover was successfully sender.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)