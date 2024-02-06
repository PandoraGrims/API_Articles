from django.urls import path
from django.views.generic import RedirectView

from webapp.views.articles_view import \
    ArticleListView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, \
    ArticleDeleteView
from webapp.views.comments_view import CommentCreateView, CommentUpdateView, CommentDeleteView

app_name = "webapp"

urlpatterns = [
    path('', RedirectView.as_view(pattern_name="webapp:index")),
    path('articles/', ArticleListView.as_view(), name="index"),
    path('articles/add/', ArticleCreateView.as_view(), name="article_add"),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="article_view"),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name="article_update_view"),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name="article_delete_view"),
    path('article/<int:pk>/comment/add/', CommentCreateView.as_view(), name="comment_add"),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name="comment_update"),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name="comment_delete"),
]
