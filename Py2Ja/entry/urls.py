from django.conf.urls import url

urlpatterns = [
    url(r'^$', "entry.views.home", name="entry_home"),
]
