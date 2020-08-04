from django.contrib import admin
from .models import UserProfile

# Register your models here.
class UserProfileAdminGrid(admin.ModelAdmin):
    list_display = ['name', 'phone', 'user']
    list_display_links = ['name', 'phone', 'user']
    list_filter = ['name', 'phone', 'user']
    search_fields = ['name', 'phone', 'user']


admin.site.register(UserProfile, UserProfileAdminGrid)