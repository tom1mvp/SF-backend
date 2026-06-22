from django.contrib.auth.hashers import make_password, check_password


from rest_framework.exceptions import ValidationError


from user.repositories.user import UserRepository
from user.serializer import UserListSerializer
from emails.services import EmailServices


class UserServices:
    @staticmethod
    def get_all_users():
        return UserRepository.get_all_users()
    
    @staticmethod
    def get_user_by_username(username):
        return UserRepository.get_user_by_username(username)
    
    @staticmethod
    def get_user_by_email(email):
        return UserRepository.get_user_by_email(email)
    

    @staticmethod
    def encrip_password(data):
        data['password'] = make_password(data.get('password'))
        
        serializer = UserListSerializer(data=data)
        
        if serializer.is_valid():
            user = serializer.save()
            
            return user
        else:
            raise ValidationError(serializer.errors)

    @staticmethod
    def login(data):
        user = UserRepository.get_user_by_username(data['username'])

        if not user:
            raise ValidationError('Error: ', 'User does not exist')

        if not check_password(data['password'], user.password):
            raise ValidationError({'error': 'Incorrect password'})
        
        return user
    
    @staticmethod
    def register(data, role_id, person_id):
        if UserRepository.get_user_by_username(data['username']):
            return {'error': 'User already exists.'}
        
        confirm_password = data['confirm_password']
        password = data['password']
        
        if password != confirm_password:
            return {'error': 'Passwords do not match'}
        
        hashed_password = make_password(data['password'])
        
        user =  UserRepository.create_user(
            username=data['username'],
            password=hashed_password,
            profile_picture=data['profile_picture'],
            role_id=role_id,
            person_id=person_id
        )
        
        EmailServices.send_welcome_email(
        to_email=user.person.email,
        username=user.username
    )
        
        return user
    
    @staticmethod
    def update_user(data, user_id):
        required_fields = ['username', 'password']
        
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'El campo {field} es obligatorio'})
            
        hashed_password = make_password(data['password'])
            
        user = UserRepository.update_user(
            user_id=user_id,
            username=data['username'],
            password=hashed_password,
            profile_picture=data.get('profile_picture', '')
        )
        
        return user

        
    @staticmethod
    def delete_user(user_id):
        return UserRepository.delete_user(user_id)
    
    @staticmethod
    def recover_user(email):
        user = UserRepository.recover_user(email)
    
        EmailServices.send_account_reactivated_confirmation(
            to_email=user.person.email,
            username=user.username
        )
    
        return user

    
    @staticmethod
    def recover_password(user_id, data):
        confirm_password = data['confirm_password']
        password = data['password']
        
        if password != confirm_password:
            return {'error': 'Passwords do not match'}
        
        hashed_password = make_password(data['password'])
        
        user = UserRepository.recover_password(
            user_id=user_id,
            password=hashed_password
        )
        
        return user
