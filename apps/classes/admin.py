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
    list_display = ('id', 'name', 'get_class', 'display_instructors', 'description', 'schedule', 'created_at', 'updated_at')
    list_filter = ('_class', 'instructors', 'schedule', 'created_at', 'updated_at')
    ordering = ('name', 'created_at', 'updated_at')
    search_fields = ('name', '_class__name', 'instructors__username', 'schedule', 'created_at', 'updated_at')
    
    def get_class(self, obj):
        """Custom method to display the related class"""
        return obj._class.name if obj._class else None
    get_class.short_description = 'Class'
    get_class.admin_order_field = '_class__name'
    
    def display_instructors(self, obj):
        """Custom method to display instructors"""
        return ", ".join([instructor.username for instructor in obj.instructors.all()[:3]])
    display_instructors.short_description = 'Instructors'