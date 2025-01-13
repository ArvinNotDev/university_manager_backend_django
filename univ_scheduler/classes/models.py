from django.db import models
from accounts.models import User
from departments.models import Department
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        abstract = True


class Class(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name=_("Department"), db_index=True)
    description = models.TextField(verbose_name=_("Description"))

    class Meta:
        managed = True
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

    def __str__(self):
        return f"{self.course.name} - {', '.join([instructor.username for instructor in self.instructors.all()])}"


class Course(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    code = models.CharField(max_length=10, unique=True, verbose_name=_("Code"), db_index=True)
    _class = models.ManyToManyField(Class, on_delete=models.CASCADE, verbose_name=_("Class"), db_index=True)
    instructors = models.ManyToManyField(User, limit_choices_to={'is_teacher': True}, verbose_name=_("Instructors"))
    description = models.TextField(verbose_name=_("Description"))
    schedule = models.TimeField(verbose_name=_("Schedule"), db_index=True)

    class Meta:
        managed = True
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name
