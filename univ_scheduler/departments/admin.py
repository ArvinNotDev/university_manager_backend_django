from django.contrib import admin
from models import Department, DepartmentManager

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description', 'created_at')
    ordering = ('name',)

@admin.register(DepartmentManager)
class DepartmentManagerAdmin(admin.ModelAdmin):
    list_display = ('department', 'manager_name', 'start_date')
    search_fields = ('manager_name', 'department__name')
    ordering = ('manager_name',)

