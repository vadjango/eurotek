from django.core.management.base import BaseCommand, CommandError
from report.auth.user.models import User


class Command(BaseCommand):
    help = "This command is developed for creating superusers"

    def handle(self, *args, **kwargs):
        while True:
            employee_id = input("Employee_id: ")
            if not employee_id.isnumeric():
                self.stderr.write("Employee id must be a number!")
            else:
                break
        first_name = input("Firstname (leave blank to set as 'admin'): ")
        last_name = input("Lastname (leave blank to set as ''): ")
        phone_number = input("Phone number (leave blank to set as ''): ")
        password = input("Password: ")
        try:
            u = User.objects.create_superuser(
                employee_id=employee_id,
                first_name=first_name or "admin",
                last_name=last_name or "",
                phone_number=phone_number or "",
                password=password)
            self.stdout.write(self.style.SUCCESS(f"The user {u} was successfully created!"))
        except Exception as e:
            raise CommandError(e)
