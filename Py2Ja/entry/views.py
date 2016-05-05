from django.shortcuts import render
from django.views.decorators.cache import cache_page

from models import AgentIP


#@cache_page(60 * 60)
def home(request):
    addr = request.META["REMOTE_ADDR"]
    if AgentIP.objects.filter(ip=addr).exists():
        flag = "true"
    else:
        flag = "false"
        new_ip = AgentIP(ip=addr)
        new_ip.save()
    return render(request, "entry_home.html", {"flag": flag})
