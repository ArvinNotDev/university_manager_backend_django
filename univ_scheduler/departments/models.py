from django.db import models
from accounts.models.User import User
from django.utils.translation import ugettext_lazy as _
import uuid


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        abstract = True


class DepartmentManager(BaseModel):
    user = models.OneToOneField(User, limit_choices_to={"is_employee": True}, on_delete=models.CASCADE, verbose_name=_("User"), db_index=True)


class Department(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("ID"), db_index=True)
    name = models.CharField(max_length=100, verbose_name=_("Name"), db_index=True)
    department_manager = models.OneToOneField(DepartmentManager, on_delete=models.CASCADE, verbose_name=_("Department manager"), db_index=True)
    description = models.TextField(max_length=200, verbose_name=_("Description"))

    def __str__(self):
        return self.name