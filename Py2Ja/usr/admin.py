from django.contrib import admin

from models import Hacker


class HackerAdmin(admin.ModelAdmin):
    list_display = (
        "sex", "hacker", "age", "commit_code", "commit_blog",
    )

    list_filter = (
        "sex",
    )


admin.site.register(Hacker, HackerAdmin)
