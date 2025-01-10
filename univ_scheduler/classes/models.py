from django.db import models
from accounts.models import User
from departments.models import Department


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    credits = models.IntegerField()

    def __str__(self):
        return self.name


class Class(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructors = models.ManyToManyField(User, limit_choices_to={'is_teacher': True})
    schedule = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course.name} - {', '.join([instructor.username for instructor in self.instructors.all()])}"
