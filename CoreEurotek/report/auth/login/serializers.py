from rest_framework_simplejwt import exceptions
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.settings import api_settings


# class AbstractLoginSerializer(TokenObtainSerializer):
#     def validate(self, attrs):
#         authentication_kwargs = {
#             self.username_field: attrs[self.username_field],
#             "password": attrs["password"]
#         }
#         try:
#             authentication_kwargs["request"] = self.context["request"]
#         except KeyError:
#             pass
#         self.user = authenticate(**authentication_kwargs)
#
#         if not api_settings.USER_AUTHENTICATION_RULE(self.user):
#             raise exceptions.AuthenticationFailed(
#                 self.error_messages["no_active_account"],
#                 "no_active_account",
#             )
#
#         return {}
