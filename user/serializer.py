from rest_framework import serializers


from user.models import Role, User


class RoleListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields='__all__'
        
class UserListSerializer(serializers.ModelSerializer):
    role_name = serializers.SerializerMethodField()
    person_id = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    document_number = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    phone_number = serializers.SerializerMethodField()
    
    class Meta:
        model=User
        fields = [
            'id',
            'username',
            'role_name',
            'person_id',
            'first_name',
            'last_name',
            'document_number',
            'email',
            'phone_number'
        ]
    
    def get_role_name(self, obj):
        return obj.role.name
    
    def get_person_id(self, obj):
        return obj.person.id
    
    def get_first_name(self, obj):
        return obj.person.first_name
    
    def get_last_name(self, obj):
        return obj.person.last_name
    
    def get_email(self, obj):
        return obj.person.email
    
    def get_document_number(self, obj):
        return obj.person.document_number
    
    def get_phone_number(self, obj):
        return obj.person.phone_number