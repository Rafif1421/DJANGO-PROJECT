from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("reqister/", views.register_user, name="register"),
    path("login/", views.login_user, name="login")
]