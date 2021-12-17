from django.contrib import admin

from .models import Project


"""class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

"""
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'languages', 'repo', 'image')#'pub_date', 'was_published_recently')
    #list_filter = ['pub_date']
    search_fields = ['title', 'languages']
    fieldsets = [
        (None,               {'fields': ['title', 'description', 'languages', 'repo', 'image_path', 'image_tag']}),
        #('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    #inlines = [ChoiceInline]

    readonly_fields = ['image_tag', 'languages']

admin.site.register(Project, ProjectAdmin)