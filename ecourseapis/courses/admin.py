from django.contrib import admin
from django.db.models import Count
from django.template.response import TemplateResponse
from django.utils.safestring import mark_safe
from unicodedata import category

from courses.models import Category, Course, Lesson, Tag, Comment
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Lesson
        fields = '__all__'

class CourseAdmin (admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_date', 'active']
    search_fields = ['subject']
    list_filter = ['id', 'subject', 'created_date']
    readonly_fields = ['image_view']

    def image_view(self, course):
        return mark_safe(f"<img src='/static/{course.image.name}' width='120' />")

    class Media:
        css = {
            'all': ('/static/css/styles.css', )
        }

class LessonAdmin(admin.ModelAdmin):
    form = LessonForm
    list_display = ['id', 'subject']
    search_fields = ['subject']
    list_filter = ['id', 'subject']
    readonly_fields = ['image_view']

    def image_view(self, lesson):
        return mark_safe(f"<img src='/static/{lesson.image.name}' width='120' />")

class CourseAppAdminSite(admin.AdminSite):
    site_header = 'Hệ thống khoá học trực tuyến'

    def get_urls(self):
        return [path('course-stats/', self.stats_view)] + super().get_urls()

    def stats_view(self, request):
        stats = Category.objects.annotate(count=Count('course')).values('id', 'name', 'count')

        return TemplateResponse(request, 'admin/stats.html', {'stats':stats})


admin_site = CourseAppAdminSite(name = 'eCourse')

admin_site.register(Category)
admin_site.register(Tag)
admin_site.register(Comment)
admin_site.register(Course, CourseAdmin)
admin_site.register(Lesson, LessonAdmin)
