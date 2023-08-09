from report.auth.user.serializers import UserSerializer
from report.auth.user.models import User


class RegisterSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ['employee_id', 'first_name', 'last_name', 'password', 'phone_number', 'avatar']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
