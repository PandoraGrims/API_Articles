from django.urls import path

from api_v2.views import get_csrf_token
from api_v2.views import ArticleView

app_name = "api_v2"

urlpatterns = [
    path("articles/", ArticleView.as_view(), name="articles"),
    path("articles/<int:pk>/", ArticleView.as_view(), name="article"),
    path("get-csrf-token/", get_csrf_token)
]
