import logging
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from report.auth.user.models import User

logger = logging.getLogger(__name__)


class UserSerializer(serializers.ModelSerializer):
    token_serializer = RefreshToken
    password = serializers.CharField(write_only=True, required=True, min_length=8, max_length=20)

    class Meta:
        model = User
        fields = ["id", "employee_id", "avatar", "first_name", "last_name", "phone_number", "password", "created_at",
                  "edited_at"]
        read_only_fields = ["id", "created_at", "edited_at"]

    def create(self, validated_data):
        logger.info(f"Created user {validated_data['employee_id']} {validated_data['first_name']} {validated_data['last_name']}")
        return User.objects.create_user(**validated_data)
