from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse,HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api_v2.serializers import  ArticleModelSerializer
from webapp.models import Article

@ensure_csrf_cookie
def get_csrf_token(request, *args, **kwargs):
    if request.method == "GET":
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


class ArticleView(APIView):
    serializer_class = ArticleModelSerializer

    def get(self, request, *args, **kwargs):
        articles = Article.objects.order_by("-created_at")
        article_data = self.serializer_class(articles, many=True).data
        return Response(article_data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        article = serializer.save()
        return Response(self.serializer_class(article).data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=article)
        serializer.is_valid(raise_exception=True)
        article = serializer.save()
        return Response(self.serializer_class(article).data, status=status.HTTP_200_OK)
        # else:
        #     return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

