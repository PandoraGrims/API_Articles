from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import CommentForm
from webapp.models import Article, Comment


class CommentCreateView(CreateView):
    form_class = CommentForm
    template_name = "comments/comment_create.html"

    # def form_valid(self, form):
    #     article = get_object_or_404(Article, pk=self.kwargs.get("pk"))
    #     form.instance.article = article
    #     return super().form_valid(form)

    def form_valid(self, form):
        article = get_object_or_404(Article, pk=self.kwargs.get("pk"))
        comment = form.save(commit=False)
        comment.article = article
        comment.author = self.request.user
        comment.save()
        # form.save_m2m()
        return redirect("webapp:article_view", pk=article.pk)

    # def get_success_url(self):
    #     return reverse("webapp:article_view", kwargs={"pk": self.object.article.pk})


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "comments/update_comment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["message"] = "test"
        return context

    def get_success_url(self):
        return reverse("webapp:article_view", kwargs={"pk": self.object.article.pk})


class CommentDeleteView(DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse("webapp:article_view", kwargs={"pk": self.object.article.pk})

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
