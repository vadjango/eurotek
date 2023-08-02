from django.db import models
from phonenumber_field import modelfields
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.validators import MaxValueValidator
from django.http import Http404


def image_path(instance, filename):
    return f"{instance.user.employee_id}/{filename}"


class UserManager(BaseUserManager):
    def get_object_by_employee_id(self, value):
        try:
            return self.get(employee_id=value)
        except (ValueError, TypeError, ObjectDoesNotExist):
            raise Http404

    def create_user(self, employee_id=None, first_name=None, last_name=None, phone_number=None, password=None,
                    **kwargs):
        if employee_id is None:
            raise ValidationError(f"User must have an employee id!")
        if first_name is None:
            raise ValidationError(f"User must have a firstname!")
        if last_name is None:
            raise ValidationError(f"User must have a lastname!")
        if phone_number is None:
            raise ValidationError(f"User must have a phone number!")
        if password is None:
            raise ValidationError(f"User must have a password!")
        user = self.model(employee_id=employee_id,
                          first_name=first_name,
                          last_name=last_name,
                          phone_number=phone_number,
                          **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, employee_id=None, first_name=None, last_name=None, phone_number=None, password=None,
                         **kwargs):
        if employee_id is None:
            raise ValidationError(f"Superuser must have an employee id!")
        if first_name is None:
            raise ValidationError(f"Superuser must have a firstname!")
        if last_name is None:
            raise ValidationError(f"Superuser must have a lastname!")
        if phone_number is None:
            raise ValidationError(f"Superuser must have a phone number!")
        if password is None:
            raise ValidationError(f"Superuser must have a password!")
        user = self.model(employee_id=employee_id,
                          first_name=first_name,
                          last_name=last_name,
                          phone_number=phone_number,
                          **kwargs)
        user.set_password(password)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    employee_id = models.IntegerField(primary_key=True, validators=[MaxValueValidator(99999)])
    avatar = models.ImageField(null=True, blank=True, upload_to=image_path)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    phone_number = modelfields.PhoneNumberField()
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "employee_id"

    objects = UserManager()

    def __str__(self):
        return f"Employee_id: {self.employee_id}"
