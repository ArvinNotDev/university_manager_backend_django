from django.contrib import admin
from .models import Class, Course


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'description', 'created_at', 'updated_at')
    list_filter = ('department', 'created_at', 'updated_at')
    ordering = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'department', 'created_at', 'updated_at')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', '_class', 'instructors', 'description', 'schedule', 'created_at', 'updated_at')
    list_filter = ('_class', 'instructors', 'schedule', 'created_at', 'updated_at')
    ordering = ('name', 'created_at', 'updated_at')
    search_fields = ('name', '_class', 'instructors', 'schedule', 'created_at', 'updated_at')
