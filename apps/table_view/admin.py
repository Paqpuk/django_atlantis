from django.contrib import admin

# Register your models here.
from .models import HILs
from simple_history.admin import SimpleHistoryAdmin

@admin.register(HILs)
class HilModelAdmin(SimpleHistoryAdmin):
    list_display = ['name', 'station', 'responsible']
# Register your models here.
