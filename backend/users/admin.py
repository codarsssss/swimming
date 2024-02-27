from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User  # Импортируйте вашу пользовательскую модель пользователя

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'age', 'is_staff', 'last_login', 'date_joined', 'is_active')
    # fieldsets = (
    #     (None, {'fields': ('username', 'password')}),
    #     ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
    #     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
    #                                'groups', 'user_permissions')}),
    #     ('Important dates', {'fields': ('last_login', 'date_joined')}),
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('username', 'email', 'password1', 'password2'),
    #     }),
    # )
    search_fields = ('username', 'email')
    ordering = ('username',)