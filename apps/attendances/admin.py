from django.contrib import admin
from .models import AttendanceSession, AttendanceRecord


@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('student', 'session', 'present')
    list_filter = ('present', 'session__course', 'session__class_obj')
    search_fields = ('student__username', 'student__email', 'session__course__name', 'session__class_obj__name')
    ordering = ('session__created_at', 'student')
    autocomplete_fields = ('student', 'session')


@admin.register(AttendanceSession)
class AttendanceSessionAdmin(admin.ModelAdmin):
    list_display = ('course', 'class_obj', 'schedule', 'created_at')
    list_filter = ('course', 'class_obj', 'schedule')
    search_fields = ('course__name', 'class_obj__name', 'schedule__course__name')
    ordering = ('created_at',)
    autocomplete_fields = ('course', 'class_obj', 'schedule')
    inlines = []

