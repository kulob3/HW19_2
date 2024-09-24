from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class Admin(admin.ModelAdmin):
    list_display = ["title", "slug", "content", "preview", "created_at", "is_published", "views"]



