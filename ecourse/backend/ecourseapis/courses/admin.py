from django.contrib import admin
from django.utils.html import mark_safe
from .models import Category, Course, Lesson, Tag


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'active', 'create_date', 'updated_date']
    search_fields = ['id', 'subject', 'content']
    search_help_text = 'Tìm kiếm bằng id, tên subject hoặc nội dung'
    list_filter = ['subject', 'create_date', 'active']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active', 'create_date', 'updated_date']
    search_fields = ['id', 'name']
    search_help_text = 'Tìm kiếm bằng id hoặc tên danh mục'
    list_filter = ['name', 'create_date', 'active']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'category', 'active', 'create_date', 'updated_date']
    search_fields = ['id', 'subject', 'description']
    search_help_text = 'Tìm kiếm bằng id, tên khóa học hoặc mô tả'
    list_filter = ['subject', 'category', 'create_date', 'active']
    readonly_fields = ['image_view']

    def image_view(self, obj):
        if obj and obj.image:
            return mark_safe(f'<img src="/static/{obj.image.name}" width="200" />')
        return ''


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active', 'create_date', 'updated_date']
    search_fields = ['id', 'name']
    search_help_text = 'Tìm kiếm bằng id hoặc tên tag'
    list_filter = ['name', 'create_date', 'active']


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag, TagAdmin)