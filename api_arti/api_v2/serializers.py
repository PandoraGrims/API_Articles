from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from webapp.models import Article, Tag, Comment


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50, required=True)
    content = serializers.CharField(max_length=2000, required=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def validate(self, attrs):
        return super().validate(attrs)

    def validate_title(self, value):
        if len(value) < 5:
            raise ValidationError("Длина меньше 5 символов не разрешена")
        return value

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    # test = serializers.CharField(max_length=15, write_only=True)



class AuthorModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email"]

class TagModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ["id", "name"]


class ArticleModelSerializer(serializers.ModelSerializer):
    author = AuthorModelSerializer(required=False)

    def to_representation(self, instance):
        print(instance)
        data = super().to_representation(instance)
        print(data)
        data['tags'] = TagModelSerializer(instance.tags.all(), many=True).data
        print(data)
        return data

    def save(self):
        super().save()

    class Meta:
        model = Article
        fields = ["id", "tags", "author", "created_at", "updated_at", "title", "content"]
        read_only_fields = ("id", "author", "created_at", "updated_at")


    def validate_title(self, value):
        if len(value) < 5:
            raise ValidationError("Длина меньше 5 символов не разрешена")
        return value
