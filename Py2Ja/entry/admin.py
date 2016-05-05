from django.contrib import admin

from models import AgentIP


class AgentIPAdmin(admin.ModelAdmin):
    list_display = (
        "ip",
    )


admin.site.register(AgentIP, AgentIPAdmin)
