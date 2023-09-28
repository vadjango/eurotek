from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class OnesignalUserProfile(models.Model):
    user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE)
    onesignal_app_id = models.CharField(max_length=36)
