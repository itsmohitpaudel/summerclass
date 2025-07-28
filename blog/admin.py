from django.contrib import admin
from . models import Blog, BlogCategory


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BlogAdmin(admin.ModelAdmin):
    exclude = ('created_at',)
    list_display = ('title', 'category', 'description', 'status')
    search_fields = ("title",)
    list_filter = ("category",)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(BlogCategory, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
