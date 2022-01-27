from django.contrib import admin

from .models import Summary, NavBarButton, DropDownButton


class SummaryAdmin(admin.ModelAdmin):
    list_display = ('heading', 'content')
    search_fields = ['heading']
    fieldsets = [
        (None, {'fields': ['heading', 'content']}),
    ]


admin.site.register(Summary, SummaryAdmin)


class DropDownButtonInline(admin.TabularInline):
    model = DropDownButton
    extra = 10


class NavBarButtonAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'has_dropdown')
    search_fields = ['title', 'page', 'has_dropdown']
    fieldsets = [
        (None, {'fields': ['title', 'page', 'has_dropdown']}),
    ]

    inlines = [DropDownButtonInline]


admin.site.register(NavBarButton, NavBarButtonAdmin)
