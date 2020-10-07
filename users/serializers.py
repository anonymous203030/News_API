
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed


from .models import User, UserProfile
from django.contrib import auth


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, min_length=8)

    class Meta:
        model=User
        fields = ('id', 'email', 'username', 'password', 'is_upgraded', )
        ordering = ['-id']


    def validate(self, attrs):
        email=attrs.get('email', '')
        username=attrs.get('username', '')
        is_upgraded=attrs.get('is_upgraded', '')

        if not username.isalnum():
            raise serializers.ValidationError('The Username Should'
                                              'Only Contain Alpha Characters')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=50, min_length=3, write_only=True)
    username = serializers.CharField(read_only=True)


    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'username', )
        ordering = ['-id']

    def validate(self,attrs):
        email=attrs.get('email', '')
        password =attrs.get('password','')


        user = auth.authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials,try again')
        if not user.is_active:
            raise AuthenticationFailed('Account Disabled')
        if not user.is_verified:
            raise AuthenticationFailed('Not Verified')
        return {
            'email': user.email,
            'username':user.username,
            # 'password':user.password
        }
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_active', 'is_verified', 'is_staff', 'created_at', 'updated_at', )
        ordering = ['-id']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id','image', 'first_name', 'last_name', 'about', 'birthday', 'gender', 'owner',)
        ordering = ['-id']
