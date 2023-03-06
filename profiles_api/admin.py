from django.contrib import admin
from profiles_api.models import UserProfile
from django.contrib.auth.admin import UserAdmin
# Register your models here.

# class AdminUser(UserAdmin):
#     ordering = ('email', 'name')
#     list_display = ('email', 'name')
#     search_fields = ('email', 'name')


admin.site.register(UserProfile)
