from django.db import models
from accounts.models import User
from departments.models import Branch

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    credits = models.IntegerField()

    def __str__(self):
        return self.name


class Rooms(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    location = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructors = models.ManyToManyField(User, limit_choices_to={'is_teacher': True})
    schedule = models.CharField(max_length=100)
    room = models.ForeignKey('Rooms', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.course.name} - {', '.join([instructor.username for instructor in self.instructors.all()])}"
