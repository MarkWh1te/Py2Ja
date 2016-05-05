# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page

from upload_avatar import get_uploadavatar_context

from models import Hacker


def check_email(email):
    import re
    pattern = "^([a-zA-Z0-9_])+@([a-zA-Z0-9])+((\.[a-zA-Z0-9]{2,3}){1,2})$"
    if isinstance(re.match(pattern, email), type(None)):
        return True
    else:
        return False


# @cache_page(60 * 15)
def register(request):
    if request.method == "GET":
        return render(request, "user_register.html")
    else:
        if not request.POST.get("inputUsername") or not request.POST.get("inputEmail") \
                or not request.POST.get("inputPassword") or not request.POST.get("inputRePassword") \
                or not request.POST.get("inputSex") or not request.POST.get("inputAge"):
            return redirect("/user/register")
        elif check_email(request.POST["inputEmail"].strip()):
            return redirect("/user/register")
        elif request.POST["inputPassword"].strip() != request.POST["inputRePassword"].strip():
            return redirect("/user/register")
        else:
            username = request.POST["inputUsername"].strip()
            email = request.POST["inputEmail"].strip()
            password = request.POST["inputPassword"].strip()
            new_user = User.objects.create_user(username=username, email=email, password=password)
            sex = request.POST["inputSex"].strip()
            age = request.POST["inputAge"].strip()
            avatar_name = username+"-40"
            new_hacker = Hacker(hacker=new_user, sex=sex, age=age, avatar_name=avatar_name)
            new_hacker.save()
        return render(request, "user_register.html")


def user_login(request):
    if request.is_ajax() and request.method == "POST":
        username = request.POST["username"].strip()
        password = request.POST["password"].strip()
        if User.objects.filter(username=username).exists():
            user = authenticate(username=username, password=password)
            if user is None:
                return HttpResponse("登陆密码错误, 请您更正！")
            elif user.is_active:
                login(request, user)
                return HttpResponse("登陆成功！")
        else:
            return HttpResponse("用户未注册，请您先注册！")


def user_logout(request):
    if request.is_ajax():
        logout(request)
        return HttpResponse("登出成功！")


def user_reset_password(request):
    return HttpResponse()


@login_required()
# @cache_page(60 * 15)
def user_home(request, hacker):
    hacker = Hacker.objects.get(hacker=request.user)
    collected_blogs = hacker.collect_blogs.all()
    collected_codesnippts = hacker.collect_codesnippts.all()
    return render(request, "user_home.html", {"collected_blogs": collected_blogs,
                                              "collected_codesnippts": collected_codesnippts})


@login_required()
# @cache_page(60 * 15)
def upload(request):
    return render_to_response('user_avatar_upload.html',
                              get_uploadavatar_context(),
                              context_instance=RequestContext(request))


def fix_image_name(request):
    if request.is_ajax():
        image_url = request.GET["image_url"].strip()
        import re
        image_name = re.findall("^/media/uploaded_images/(.*?)\.jpg$", image_url)[0]
        username = request.user.username
        import os
        path = os.getcwd()
        # os.rename(path+"/media/cropped_avatars/%s-40.jpeg" % image_name,
        #           path+"/media/cropped_avatars/%s-40.jpeg" % username)
        # os.rename(path+"/media/cropped_avatars/%s-120.jpeg" % image_name,
        #           path+"/media/cropped_avatars/%s-120.jpeg" % username)
        # import commands
        # commands.getstatusoutput("sudo chown summy:summy "+path+"/media/uploaded_images/%s.jpg" % image_name)
        # commands.getstatusoutput("sudo chmod 755 "+path+"/media/uploaded_images/%s.jpg" % image_name)
        os.rename(path+"/media/uploaded_images/%s.jpg" % image_name,
                  path+"/media/uploaded_images/%s.jpg" % username.encode("utf-8"))
        return HttpResponse("Success!")
