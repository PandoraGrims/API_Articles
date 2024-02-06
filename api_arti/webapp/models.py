from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        abstract = True


class Article(AbstractModel):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Название")

    content = models.TextField(max_length=2000, verbose_name="Контент")
    tags = models.ManyToManyField('webapp.Tag', related_name='articles', blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT,
                               default=1, related_name="articles", verbose_name="Автор")

    def __str__(self):
        return f"{self.pk} {self.title}: {self.author}"

    def get_absolute_url(self):
        return reverse("webapp:article_view", kwargs={"pk": self.pk})  # article/5/

    class Meta:
        db_table = "articles"
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        permissions = [
            ('write_rate', 'Написать рецензию')
        ]


class Comment(AbstractModel):
    article = models.ForeignKey('webapp.Article', related_name='comments', on_delete=models.CASCADE,
                                verbose_name='Статья')
    text = models.TextField(max_length=400, verbose_name='Комментарий')
    author = models.ForeignKey('auth.User', on_delete=models.SET_DEFAULT,
                               default=1, related_name="comments", verbose_name="Автор")

    def __str__(self):
        return self.text[:20]


class Tag(AbstractModel):
    name = models.CharField(max_length=31, verbose_name='Тег')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tags"
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
