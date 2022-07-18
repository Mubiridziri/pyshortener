from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Link


def index(request):
    alive_links_list = Link.objects.order_by('-pub_date')[:5]
    context = { 'alive_links_list': alive_links_list, 'host': request.build_absolute_uri('/')}
    return render(request, 'index.html', context)


def create(request):
    link_name = request.POST['name']
    original_link = request.POST['original_link']
    link = Link()
    link.name = link_name
    link.original_link = original_link
    link.pub_date = timezone.now()
    link.save()
    return HttpResponseRedirect('/')


def open_link(request, link_id):
    link = get_object_or_404(Link, pk=link_id)
    return HttpResponseRedirect(link.original_link)
