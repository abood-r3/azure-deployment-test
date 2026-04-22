from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Client, User


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("name", "slug")


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("email", "first_name", "last_name", "client", "role", "is_active", "is_staff")
    list_filter = ("role", "is_active", "is_staff", "client")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Client & Role", {"fields": ("client", "role")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2", "client", "role")}),
    )
