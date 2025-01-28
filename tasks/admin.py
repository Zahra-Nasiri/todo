from django.contrib import admin

from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'due_date',
        'completed',
        'created_at',
        'updated_at',
    )
    list_filter = ('completed', )
    search_fields = (
        'title',
        'description',
    )

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'due_date', 'completed')
        }),
        ('Advanced Options', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse', ),
        }),
    )

    readonly_fields = ('created_at', 'updated_at')
