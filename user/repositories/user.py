from user.models import User, Role


from people.models import Person


class UserRepository:
    @staticmethod
    def get_all_users():
        return User.objects.all()
    
    @staticmethod
    def get_user_by_username(username):
        return User.objects.filter(username__icontains=username).first()
    
    @staticmethod
    def get_user_by_email(email):
        return User.objects.filter(person__email__iexact=email).first()
    
    @staticmethod
    def create_user(
        username,
        password,
        profile_picture,
        role_id,
        person_id,
        is_active=True
    ):
        
        person = Person.objects.filter(id=person_id).first()
        
        if not person: raise ValueError('Person not found')
        
        role = Role.objects.filter(id=role_id).first()
        
        if not role: raise ValueError('Role not found')
        
        new_user = User.objects.create(
            username=username,
            password=password,
            profile_picture=profile_picture,
            role=role,
            person=person,
            is_active=is_active
        )
        
        return new_user
    
    @staticmethod
    def update_user(
        user_id,
        username,
        password,
        profile_picture
    ):
        user = User.objects.filter(id=user_id).first()
        
        if not user: raise ValueError('User not found')

        user.username = username
        user.password = password
        user.profile_picture = profile_picture
        
        user.save()
        
        return user
        
    @staticmethod
    def delete_user(user_id):
        user = User.objects.filter(id=user_id).first()

        if not user: raise ValueError('User not found')
        
        if user.is_active:
            user.is_active = False
            
            user.save()
            return user

    @staticmethod
    def recover_user(
        email
    ):
        user = User.objects.filter(person__email__iexact=email).first()
    
        if not user: 
            raise ValueError('No user found associated with this email')

        if not user.is_active:
            user.is_active = True
            
            user.save()

        return user
    
    @staticmethod
    def recover_password(user_id, password):
        user = User.objects.filter(id=user_id).first()
        
        if not user:
            raise ValueError('No user found associated with this email')
        
        user.password = password
        
        user.save()
        
        return user
    