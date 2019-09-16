from django.contrib import admin
from webapp.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'description', 'status', 'full_description', 'finish_at']
    list_filter = ['status', 'description']
    list_display_links = ['pk', 'description']
    search_fields = ['status']
    fields = ['description', 'status', 'full_description', 'finish_at']

admin.site.register(Article, ArticleAdmin)