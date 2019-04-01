from django.contrib import admin
from .models import UserResponse
from import_export.admin import ImportExportModelAdmin

@admin.register(UserResponse)
class ViewAdmin(ImportExportModelAdmin):
    pass
