from django.contrib import admin

from .models import *


@admin.register(Emaildata)
class EmaildataAdmin(admin.ModelAdmin):
    list_display = ('created', 'sender', 'from_email', 'status')
    list_display_links = ('created', 'sender', 'from_email')
    ordering = ['-created']
