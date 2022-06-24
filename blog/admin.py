from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost, Comment


@admin.register(BlogPost)
class BlogAdmin(SummernoteModelAdmin):
    """
    Use Summernote for blog admin
    """
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'status', 'publish_date')
    search_fields = ['title', 'content']
    list_filter = ('status', 'publish_date')
    summernote_fields = ('content')
    readonly_fields = ('slug',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Ability to manage comments in admin panel
    """
    list_display = ('name', 'body', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        approval of comments
        """
        queryset.update(approved=True)
