from django.contrib import admin
from .models import Department, DepartmentManager

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description', 'created_at')
    ordering = ('name',)

@admin.register(DepartmentManager)
class DepartmentManagerAdmin(admin.ModelAdmin):
    list_display = ('department', 'get_manager_name', 'get_start_date', 'created_at', 'updated_at')
    search_fields = ('user__username', 'department__name', 'created_at', 'updated_at')
    ordering = ('user__username', 'created_at', 'updated_at')
    
    def get_manager_name(self, obj):
        """Custom method to display manager's name"""
        if obj.user:
            return obj.user.get_full_name() or obj.user.username
        return "No manager assigned"
    get_manager_name.short_description = 'Manager Name'
    
    def get_start_date(self, obj):
        """Custom method to display start date"""
        return obj.start_date if hasattr(obj, 'start_date') else "N/A"
    get_start_date.short_description = 'Start Date'