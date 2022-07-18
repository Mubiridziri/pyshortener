from django.urls import path

from .controllers import link_controller, user_controller

urlpatterns = [
    path("", link_controller.index, name="index"),
    path("create", link_controller.create, name="create"),
    path("l/<int:link_id>", link_controller.open_link, name="open_shorted_link"),
    path("remove/<int:link_id>", link_controller.remove_link, name="remove_shorted_link"),
    path("login", user_controller.login_user, name="login_page"),
    path("logout", user_controller.logout_user, name="logout_page"),
    path("reg", user_controller.reg_user, name="reg_page")
]
