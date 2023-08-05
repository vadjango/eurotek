from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class LoginTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["phone_number"] = user.phone_number.as_e164
        return token

