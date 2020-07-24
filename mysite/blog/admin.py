from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','slug', 'author', 'created']
    list_filter = ['created']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}

