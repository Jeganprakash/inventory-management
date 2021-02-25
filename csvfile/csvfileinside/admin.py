from django.contrib import admin
from .models import *

from import_export.admin import ImportExportModelAdmin
from csvfileinside.models import Profile

@admin.register(Profile)
class Profileadmin(ImportExportModelAdmin):
    #list_display=("name","email","address","phone","profile")
    pass