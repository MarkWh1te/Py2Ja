# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page

from models import CodeSnippet
from usr.models import Hacker


# @cache_page(60 * 15)
def list_codes(request):
    cpp_snippets = CodeSnippet.objects.filter(type="C++").order_by("-create_timestamp")
    java_snippets = CodeSnippet.objects.filter(type="Java").order_by("-create_timestamp")
    python_snippets = CodeSnippet.objects.filter(type="Python").order_by("-create_timestamp")
    php_snippets = CodeSnippet.objects.filter(type="PHP").order_by("-create_timestamp")
    javascript_snippets = CodeSnippet.objects.filter(type="JavaScript").order_by("-create_timestamp")
    sql_snippets = CodeSnippet.objects.filter(type="SQL").order_by("-create_timestamp")
    hacker_stars = Hacker.objects.all().order_by("-commit_code")[:6]
    return render(request, "program_list_codes.html", {"cpp_snippets": cpp_snippets,
                                                       "java_snippets": java_snippets,
                                                       "python_snippets": python_snippets,
                                                       "php_snippets": php_snippets,
                                                       "javascript_snippets": javascript_snippets,
                                                       "sql_snippets": sql_snippets,
                                                       "hacker_stars": hacker_stars})


def load_cpp(request):
    return HttpResponse()


def load_java(request):
    return HttpResponse()


def load_python(request):
    return HttpResponse()


def load_php(request):
    return HttpResponse()


def load_javascript(request):
    return HttpResponse()


def load_sql(request):
    return HttpResponse()


# @login_required()
# @cache_page(60 * 15)
def view_code(request, snippet_id):
    if request.user.is_authenticated():
        if request.is_ajax() and request.method == "GET":
            if request.GET["type"] == "1":
                current_id = request.GET["id"].strip()
                current_snippet = CodeSnippet.objects.get(id=current_id)
                current_snippet.rank += 1
                current_snippet.save()
                return HttpResponse(current_snippet.rank)
            elif request.GET["type"] == "2":
                current_id = request.GET["id"].strip()
                current_snippet = CodeSnippet.objects.get(id=current_id)
                current_snippet.collect_codesnippts.remove(Hacker.objects.get(hacker=request.user))
                current_snippet.collect -= 1
                current_snippet.save()
                return HttpResponse(current_snippet.collect)
            elif request.GET["type"] == "3":
                current_id = request.GET["id"].strip()
                current_snippet = CodeSnippet.objects.get(id=current_id)
                current_snippet.collect_codesnippts.add(Hacker.objects.get(hacker=request.user))
                current_snippet.collect += 1
                current_snippet.save()
                return HttpResponse(current_snippet.collect)
        else:
            snippet = CodeSnippet.objects.get(id=snippet_id)
            snippet.trace += 1
            snippet.save()
            flag = "false"
            if snippet.collect_codesnippts.filter(hacker=request.user).exists():
                flag = "true"
            return render(request, "program_view_code.html", {"snippet": snippet, "flag": flag})
    else:
        return redirect("/program/code/list")


# @login_required()
# @cache_page(60 * 15)
def write_code(request):
    if request.user.is_authenticated():
        if request.is_ajax() and request.method == "POST":
            code_snippet = request.POST["inputCode"].strip()
            # import re
            # code_snippet = re.sub("<", "&lt;", code_snippet)
            code_type = request.POST["inputType"].strip()
            code_description = request.POST["inputDescription"].strip()
            code_coder = request.user.username
            # TODO
            user = User.objects.get(username=code_coder)
            hacker = Hacker.objects.get(hacker=user)
            hacker.commit_code += 1
            hacker.save()
            new_snippet = CodeSnippet(snippet=code_snippet, type=code_type,
                                      description=code_description, coder=code_coder)
            new_snippet.save()
            # TODO
            return HttpResponse("Thank you for your code!")
        else:
            return render(request, "program_write_code.html")
    else:
        return redirect("/program/code/list")


def run_python_code(request):
    if request.is_ajax() and request.method == "POST":
        code_snippet = request.POST["CodeSnippet"].strip()

        fp = open("media/files/test.py", 'w')
        fp.write(code_snippet)
        fp.write("\n")
        fp.close()

        import commands
        (status, output) = commands.getstatusoutput('python media/files/test.py')

        fp = open("media/files/test.txt", 'w')
        fp.write(output)
        fp.write("\n")
        fp.close()

        return HttpResponse(output)


def run_cpp_code(request):
    return HttpResponse()


def run_java_code(request):
    return HttpResponse()


def run_php_code(request):
    return HttpResponse()


def run_javascript_code(request):
    return HttpResponse()


def run_sql_code(request):
    return HttpResponse()
