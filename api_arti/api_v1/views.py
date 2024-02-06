from _decimal import Decimal

from django.http import HttpResponse, JsonResponse, FileResponse, HttpResponseNotAllowed
import json
from datetime import datetime

from django.views.decorators.csrf import ensure_csrf_cookie

from webapp.models import Article


@ensure_csrf_cookie
def get_csrf_token(request, *args, **kwargs):
    if request.method == "GET":
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


def echo_view(request, *args, **kwargs):
    test_dict = [
        {
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "test": 1,
            "test1": [1, 2],
            "number": Decimal("1.56"),
            # "article": Article.objects.first()
        },
    ]
    return JsonResponse(test_dict, safe=False)
    # test_dict_json = json.dumps(test_dict)
    # response = HttpResponse(test_dict_json)
    # response['Content-Type'] = 'application/json'
    # return response


def articles_view(request, *args, **kwargs):
    if request.method == "GET":
        articles = Article.objects.order_by("-created_at").values('title', 'content')
        print(articles)
        # articles_data = []
        # for article in articles:
        #     article_data = {
        #         "title": article.title,
        #         "content": article.content
        #     }
        #     articles_data.append(article_data)
        return JsonResponse(list(articles), safe=False)

    elif request.method == "POST":
        body = json.loads(request.body)
        if len(body["title"]) < 5:
            return JsonResponse({"error": "min len 5"}, status=400)
        Article.objects.create(**body)
        print(request.user)
        # Article.objects.create(title=body.title, content=body.content)
        return HttpResponse(status=201)
    return HttpResponseNotAllowed(['GET', 'POST'])
