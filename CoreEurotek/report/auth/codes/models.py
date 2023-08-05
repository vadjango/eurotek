from django.db import models
from report.auth.user.models import User
import random


# Create your models here.
class Code(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    number = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return str(self.number)

    def save(self, *args, **kwargs):
        code_string = ""
        for _ in range(10):
            num = random.randint(0, 9)
            code_string += num
        self.number = code_string
        super().save(*args, **kwargs)
