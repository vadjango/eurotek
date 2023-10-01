import logging
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from report.auth.user.models import User

logger = logging.getLogger(__name__)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["employee_id", "first_name", "last_name", "phone_number", "avatar", "created_at",
                  "edited_at"]
        read_only_fields = ["id", "created_at", "edited_at"]


