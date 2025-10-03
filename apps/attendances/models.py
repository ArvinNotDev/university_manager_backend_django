from django.db import models
from django.utils.translation import gettext_lazy as _
from base.models import BaseModel
from classes.models import Class, Course, CourseSchedule
from accounts.models import User


class AttendanceSession(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_("Course"))
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name=_("Class"))
    schedule = models.ForeignKey(CourseSchedule, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Course Schedule"))
    date = models.DateField(verbose_name=_("Date"))

    class Meta:
        verbose_name = _("Attendance Session")
        verbose_name_plural = _("Attendance Sessions")

    def __str__(self):
        return f"{self.course} - {self.date}"


class AttendanceRecord(BaseModel):
    session = models.ForeignKey(AttendanceSession, on_delete=models.CASCADE, related_name="records", verbose_name=_("Attendance Session"))
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Student"))
    present = models.BooleanField(default=False, verbose_name=_("Present"))

    class Meta:
        verbose_name = _("Attendance Record")
        verbose_name_plural = _("Attendance Records")

    def __str__(self):
        return f"{self.student} - {self.session} ({'Present' if self.present else 'Absent'})"
