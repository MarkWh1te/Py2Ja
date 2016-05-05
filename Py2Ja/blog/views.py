# -*- coding: utf-8 -*-
import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.gzip import gzip_page
from django.views.decorators.http import require_http_methods

from models import Blog, Commit
from usr.models import Hacker


@gzip_page
def list_blogs(request):
    if request.is_ajax():
        dom = ""
        request_id = request.GET["last_blog_id"].split("/")[3]
        if request_id == "1":
            dom = """
            <hr style="width: 700px;">
            <span class="badge" style="margin-left: 380px;">已经到底了！</span>
            """
            json_data = json.dumps({"DOM": dom, "Flag": "true"})
            return HttpResponse(json_data)
        else:
            if request_id == "2":
                request_id = int(request_id) - 1
                blog_ids = [request_id]
            else:
                request_id = int(request_id) - 1
                blog_ids = [request_id, request_id - 1]
            for blog_id in blog_ids:
                add_blog = Blog.objects.get(id=blog_id)

                timestamp = str(add_blog.create_timestamp)[:16]
                timestamp_half_1 = timestamp[:5]
                timestamp_half_2 = timestamp[5:16]
                timestamp = timestamp_half_1.replace('-', '月') + timestamp_half_2.replace('-', '日')

                dom += """
                <hr style="width: 700px;">
                <div class="container blog-section">
                   <div class="col-md-1 col-sm-1 col-xs-1">
                       <ul class="alert-success" style="text-align: center;"><li>%d</li><li>推荐</li></ul>
                       <ul class="alert-warning" style="text-align: center;"><li>%d</li><li>浏览</li></ul>
                   </div>
                   <div class="col-md-7 col-sm-7 col-xs-7">
                       <div class="title"><a href="/blog/view/%d">%s</a></div>
                       <div class="brief"><p>%s</p></div>
                       <div class="author"><img src="/media/cropped_avatars/%s-40.jpeg" />
                            &nbsp;&nbsp;&nbsp;&nbsp;%s发表于%s</div>
                   </div>
                </div>""" % (add_blog.rank, add_blog.trace, add_blog.id,
                             add_blog.title.encode("utf-8"), add_blog.brief.encode("utf-8"),
                             add_blog.author.encode("utf-8"), add_blog.author.encode("utf-8"),
                             timestamp)
        json_data = json.dumps({"DOM": dom, "Flag": "false"})
        return HttpResponse(json_data)
    blogs = Blog.objects.all().order_by("-create_timestamp")[:10]
    return render(request, "blog_list.html", {"blogs": blogs})


def view_blog(request, blog_id):
    if request.user.is_authenticated():
        if request.is_ajax() and request.method == "GET":
            if request.GET["type"] == "1":
                current_id = request.GET["id"].strip()
                current_blog = Blog.objects.get(id=current_id)
                current_blog.rank += 1
                current_blog.save()
                return HttpResponse(current_blog.rank)
            elif request.GET["type"] == "3":
                current_id = request.GET["commit_id"].strip()
                current_commit = Commit.objects.get(id=current_id)
                current_commit.star += 1
                current_commit.save()
                return HttpResponse(current_commit.star)
            elif request.GET["type"] == "4":
                current_id = request.GET["id"].strip()
                current_blog = Blog.objects.get(id=current_id)
                current_blog.collect_blogs.remove(Hacker.objects.get(hacker=request.user))
                current_blog.collect -= 1
                current_blog.save()
                return HttpResponse(current_blog.collect)
            elif request.GET["type"] == "5":
                current_id = request.GET["id"].strip()
                current_blog = Blog.objects.get(id=current_id)
                current_blog.collect_blogs.add(Hacker.objects.get(hacker=request.user))
                current_blog.collect += 1
                current_blog.save()
                return HttpResponse(current_blog.collect)
        elif request.is_ajax() and request.method == "POST":
            if request.POST["type"] == "2":
                observer = User.objects.get(username=request.user.username)
                target = Blog.objects.get(id=blog_id)
                content = request.POST["content"].strip()
                new_commit = Commit(observer=observer, target=target, content=content)
                new_commit.save()

                timestamp = str(new_commit.create_timestamp)[:16]
                timestamp_half_1 = timestamp[:5]
                timestamp_half_2 = timestamp[5:16]
                timestamp = timestamp_half_1.replace('-', '月') + timestamp_half_2.replace('-', '日')

                dom = """
                <div class="commit-show-area">
                    <div class="container">
                        <div class="col-md-1 col-sm-1 col-xs-1" style="width: 70px;">
                            <img src="/media/cropped_avatars/%s-40.jpeg" />
                        </div>
                        <div class="col-md-9 col-sm-9 col-xs-9">
                            %s
                            <p>%s发表于%s<p>
                            <p><a href="javascript:void(0)">好评</a>&nbsp;&nbsp;0
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="javascript:void(0)">回复</a></p>
                        </div>
                    </div>
                </div>
                """ % (observer.username.encode("utf-8"), content.encode("utf-8"),
                       observer.username.encode("utf-8"), timestamp)
                return HttpResponse(dom)
        else:
            blog = Blog.objects.get(id=blog_id)
            blog.trace += 1
            blog.save()
            commits = Commit.objects.filter(target=blog).order_by("-create_timestamp")
            flag = "false"
            if blog.collect_blogs.filter(hacker=request.user).exists():
                flag = "true"
            return render(request, "blog_view.html", {"blog": blog, "commits": commits, "flag": flag})
    else:
        return redirect("/blog/list")


def write_blog(request):
    if request.user.is_authenticated():
        if request.is_ajax() and request.method == "POST":
            title = request.POST["inputTitle"].strip()
            brief = request.POST["inputBrief"].strip()
            content = request.POST["inputBlog"].strip()
            author = request.user.username
            hacker = Hacker.objects.get(hacker=request.user)
            hacker.commit_blog += 1
            hacker.save()
            new_blog = Blog(title=title, author=author, brief=brief,  content=content)
            new_blog.save()
            return HttpResponse("Thank you for your blog!")
        else:
            return render(request, "blog_write.html")
    else:
        return redirect("/blog/list")


def upload_image(request):
    if request.method == "POST":
        callback = request.POST.get("CKEditorFuncNum")
        try:
            import time
            import os
            path = "/media/files/upload_images/" + time.strftime("%Y%m%d%H%M%S", time.localtime())
            f = request.FILES["upload"]
            file_name = path + "_" + f.name
            des_origin_f = open(file_name, "wb+")
            for chunk in f:
                des_origin_f.write(chunk)
            des_origin_f.close()
        except Exception:
            raise http500()
        res = r"<script>window.parent.CKEDITOR.tools.callFunction("+callback+",'/"+file_name+"', '');</script>"
        return HttpResponse(res)
    else:
        return http404()


def http500():
    return HttpResponseServerError()


def http404():
    return HttpResponseBadRequest()
