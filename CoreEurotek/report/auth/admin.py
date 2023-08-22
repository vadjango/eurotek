from django.contrib import admin
from .user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("employee_id", "first_name", "last_name", "phone_number", "created_at")


admin.site.register(User, UserAdmin)
