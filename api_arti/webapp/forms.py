from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Tag, Article, Comment


def at_least_10(value):
    if len(value) < 10:
        raise ValidationError('This value is too short!')


class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=50, required=True, label="Название", validators=[at_least_10])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for v in self.visible_fields():
            if not isinstance(v.field.widget, widgets.CheckboxSelectMultiple):
                v.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Article
        fields = ["title", "content", "tags"]
        widgets = {
            "content": widgets.Textarea(attrs={"cols": 30, "rows": 5, "class": "test"}),
            "tags": widgets.CheckboxSelectMultiple
        }

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('content') and cleaned_data.get('title') and \
                cleaned_data['content'] == cleaned_data['title']:
            raise ValidationError("Text of the article should not duplicate it's title!")
        return cleaned_data


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
