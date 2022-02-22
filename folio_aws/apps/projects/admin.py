from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'description', 'languages', 'repo', 'image')
    search_fields = ['title', 'languages']
    fieldsets = [
        (None, {'fields': ['title', 'order', 'description', 'languages', 'repo',
                           'image_path', 'image_tag']}),
    ]

    readonly_fields = ['id','image_tag', 'languages']


admin.site.register(Project, ProjectAdmin)
