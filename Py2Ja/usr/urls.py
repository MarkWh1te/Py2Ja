from django.conf.urls import include, url

urlpatterns = [
    url(r'^register', "usr.views.register", name="user_register"),
    url(r'^login', "usr.views.user_login", name="user_login"),
    url(r'^logout', "usr.views.user_logout", name="user_login"),
    url(r'^home/(?P<hacker>.*)', "usr.views.user_home", name="user_home"),
    url(r'^upload-head-portrait', "usr.views.upload", name="user_avatar_upload"),
    url(r'^fix-image-name', "usr.views.fix_image_name", name="user_avatar_upload"),
]
