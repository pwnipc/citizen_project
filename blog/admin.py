from django.contrib import admin
from . models import Blog, Author

# Register your models here.

admin.site.register(Author)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_date", "published_date")
    list_display_links = ("title",)
    list_filter = ("author", "created_date")
    search_fields = ("title", "text")