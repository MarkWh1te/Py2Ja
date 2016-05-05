from django.contrib import admin

from models import CodeSnippet


class CodeSnippetAdmin(admin.ModelAdmin):
    list_display = (
        "type", "description", "coder", "create_timestamp",
    )

    list_filter = (
        "type",
    )

admin.site.register(CodeSnippet, CodeSnippetAdmin)
