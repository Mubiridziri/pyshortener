from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("l/<int:link_id>", views.open_link, name="open_shorted_link"),
    path("remove/<int:link_id>", views.remove_link, name="remove_shorted_link")
]
