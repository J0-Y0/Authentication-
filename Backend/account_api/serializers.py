from rest_framework import serializers
from account.models import User
from djoser.serializers import UserCreateSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Notes


# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = [
#             "email",
#             "first_name",
#             "password",
#         ]
#         extra_kwargs = {"password": {"write_only": True}}

#     def create(self, validated_data):

#         user = CustomUser(
#             email=validated_data["email"], first_name=validated_data["first_name"]
#         )

#         user.set_password(validated_data["password"])
#         user.save()
#         return user


class CustomUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            "email",
            "first_name",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):

        user = User(
            email=validated_data["email"], first_name=validated_data["first_name"]
        )

        user.set_password(validated_data["password"])
        user.save()
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["email"] = user.email
        token["name"] = user.first_name
        # ...

        return token


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = "__all__"
