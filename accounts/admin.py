from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'total_score', 'rank_title', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('اطلاعات بازی', {'fields': ('avatar', 'bio', 'total_score')}),
    )