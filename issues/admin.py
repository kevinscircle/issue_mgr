from django.contrib import admin
from .models import Issue

# Register your models here.
# class IssueAdmin(admin.ModelAdmin):
#     list_display = ('summary', 'status', 'priority', 'reporter', 'assignee', 'created_at', 'updated_at')
#     list_filter = ('status', 'priority', 'reporter', 'assignee')
#     search_fields = ('summary', 'description')
admin.site.register(Issue)
