import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Link


def index(request):
    latest_links = Link.objects.order_by('-pub_date')[:5]
    all_links = Link.objects.all().order_by('-pub_date').filter(pub_date__gte=datetime.date.today())
    context = { 'latest_links': latest_links, 'all_links': all_links, 'host': request.build_absolute_uri('/')}
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


def remove_link(request, link_id):
    link = get_object_or_404(Link, pk=link_id)
    link.delete()
    return HttpResponseRedirect('/')


def open_link(request, link_id):
    link = get_object_or_404(Link, pk=link_id)
    return HttpResponseRedirect(link.original_link)
