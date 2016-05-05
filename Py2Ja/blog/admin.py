from django.contrib import admin

from models import Blog, Commit


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title", "author", "rank", "trace", "create_timestamp",
    )

    list_filter = (
        "author",
    )


class CommitAdmin(admin.ModelAdmin):
    list_display = (
        "observer", "target", "star", "create_timestamp",
    )

    list_filter = (
        "target",
    )

admin.site.register(Blog, BlogAdmin)
admin.site.register(Commit, CommitAdmin)
