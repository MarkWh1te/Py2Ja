from django.conf.urls import url

urlpatterns = [
    url(r'^list', "blog.views.list_blogs", name="blog_list"),
    url(r'^view/(?P<blog_id>\d+)', "blog.views.view_blog", name="blog_view"),
    url(r'^write', "blog.views.write_blog", name="blog_write"),
    url(r'^write', "blog.views.write_blog", name="blog_write"),
    url(r'^write/image-upload/', "blog.views.upload_image", name="blog_write"),
]
