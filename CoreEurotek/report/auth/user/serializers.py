from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from report.auth.user.models import User


class UserSerializer(serializers.ModelSerializer):
    token_serializer = RefreshToken
    password = serializers.CharField(write_only=True, required=True, min_length=8, max_length=20)

    class Meta:
        model = User
        fields = ["id", "employee_id", "avatar", "first_name", "last_name", "phone_number", "password", "created_at",
                  "edited_at"]
        read_only_fields = ["id", "created_at", "edited_at"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def to_representation(self, instance):
        del instance["password"]
        data = {"user": instance}
        user = User.objects.get_object_by_employee_id(instance["employee_id"])
        token = self.token_serializer.for_user(user)
        data["refresh"] = str(token)
        data["access"] = str(token.access_token)
        return data
