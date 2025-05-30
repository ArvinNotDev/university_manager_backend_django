from django.db import models
from accounts.models import User
from django.utils.translation import gettext_lazy as _
from base.models import BaseModel
import uuid


class Department(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("ID"), db_index=True)
    name = models.CharField(max_length=100, verbose_name=_("Name"), db_index=True)
    description = models.TextField(max_length=200, verbose_name=_("Description"))

    def __str__(self):
        return self.name


class DepartmentManager(BaseModel):
    user = models.OneToOneField(User, limit_choices_to={"is_employee": True}, on_delete=models.CASCADE, verbose_name=_("User"), db_index=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name=_("Department"), db_index=True)