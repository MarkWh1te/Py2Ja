from django.conf.urls import url

urlpatterns = [
    url(r'^books/view', "knowledge.views.view", name="knowledge_view"),
]
