from django.urls import path

from api_v1.views import echo_view, articles_view, get_csrf_token

app_name = "api_v1"

urlpatterns = [
    path("echo/", echo_view, name="echo"),
    path("articles/", articles_view, name="articles"),
    path("get-csrf-token/", get_csrf_token)
]
