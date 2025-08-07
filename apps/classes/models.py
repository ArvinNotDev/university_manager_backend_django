from django.db import models
from accounts.models import User
from departments.models import Department
from django.utils.translation import gettext_lazy as _
from base.models import BaseModel
import uuid



class Class(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name=_("Department"), db_index=True)
    in_use = models.BooleanField(verbose_name=_("Class in use"), default=False)
    description = models.TextField(verbose_name=_("Description"))

    class Meta:
        managed = True
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

    def __str__(self):
        return self.name


class Course(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("ID"), db_index=True)
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    _class = models.ManyToManyField(Class, verbose_name=_("Class"))
    instructors = models.ManyToManyField(User, limit_choices_to={'is_teacher': True}, verbose_name=_("Instructors"))
    description = models.TextField(verbose_name=_("Description"))
    schedule = models.TimeField(verbose_name=_("Schedule"), db_index=True)

    class Meta:
        managed = True
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name