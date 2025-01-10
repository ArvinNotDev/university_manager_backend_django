from django.db import models
from accounts.models.User import User


class DepartmentManager(models.Model):
    user = models.OneToOneField(User, limit_choices_to={"is_employee": True}, on_delete=models.CASCADE)
    department = models.OneToOneField('Department', on_delete=models.CASCADE)


class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
