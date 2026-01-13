from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'status')
    list_filter = ('status',)
    search_fields = ('name', 'email', 'subject')
