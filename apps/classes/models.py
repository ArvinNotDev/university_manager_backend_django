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

    class Meta:
        managed = True
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name


class CourseSchedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("ID"), db_index=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='schedules', verbose_name=_("Course"))
    day_of_week = models.PositiveSmallIntegerField(
        choices=[
            (1, _("Saturday")),
            (2, _("Sunday")),
            (3, _("Monday")),
            (4, _("Tuesday")),
            (5, _("Wednesday")),
            (6, _("Thirsday")),
            (7, _("Friday")),
        ],
        verbose_name=_("Day of Week"),
        db_index=True,
    )
    start_time = models.TimeField(verbose_name=_("Start Time"), db_index=True)
    end_time = models.TimeField(verbose_name=_("End Time"), db_index=True)
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    class Meta:
        verbose_name = _("Course Schedule")
        verbose_name_plural = _("Course Schedules")
        ordering = ['day_of_week', 'start_time']
        indexes = [
            models.Index(fields=['day_of_week', 'start_time']),
        ]

    def __str__(self):
        return f"{self.course.name} on {self.day_of_week} from {self.start_time} to {self.end_time}"
