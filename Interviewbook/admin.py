from django.contrib import admin
from .models import *
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'body', 'response', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('username', 'body')
    actions = ['disapprove_comment']
    def disapprove_comment(self, request, queryset):
        queryset.update(active=False)

        
admin.site.register(InterviewResponse)
admin.site.register(Company)
admin.site.register(Comment)
