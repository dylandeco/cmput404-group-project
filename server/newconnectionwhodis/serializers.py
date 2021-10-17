from rest_framework import serializers
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer

from . import models

# https://stackoverflow.com/a/55128035
class LoginSerializer(LoginSerializer):
    email = None

class CustomRegisterSerializer(RegisterSerializer):
    email = None

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.SerializerMethodField('get_id_url')
    host = serializers.SerializerMethodField('get_host_url')
    url = serializers.SerializerMethodField('get_id_url')

    class Meta:
        model = models.Author
        fields = ('type', 'id', 'host', 'displayName', 'url', 'github', 'profileImage')

    def get_host_url(self, obj):
        return 'http://' + self.context['request'].get_host()

    def get_id_url(self, obj):
        return 'http://' + self.context['request'].get_host() + f"/{obj.type}/{obj.id}"

class PostSerializer(NestedHyperlinkedModelSerializer):
    id = serializers.SerializerMethodField('get_id_url')
    author = AuthorSerializer(many=False, read_only=True)
    # TODO: source and origin probably need to be changed
    source = serializers.SerializerMethodField('get_origin_url')
    origin = serializers.SerializerMethodField('get_origin_url')

    class Meta:
        model = models.Post
        fields = ('type', 'id', 'contentType',
            'content', 'author', 'title', 'description',
            'source', 'origin')
    
    def get_id_url(self, obj):
        host = self.context['request'].get_host()
        return f'http://{host}/author/{obj.author.id}/posts/{obj.id}'
    
    def get_origin_url(self, obj):
        return 'http://' + self.context['request'].get_host()

class CommentSerializer(NestedHyperlinkedModelSerializer):
    id = serializers.SerializerMethodField('get_id_url')
    author = AuthorSerializer(many=False, read_only=True)
    parent_lookup_kwargs = {
        'post_pk': 'post__pk',
        'author_pk': 'post__author__pk',
    }
    class Meta:
        model = models.Comment
        fields = ('type', 'author', 'comment', 'contentType', 'published', 'id')

    def get_id_url(self, obj):
        host = self.context['request'].get_host()
        return f'http://{host}/author/{obj.author.id}/posts/{obj.post.id}/comments/{obj.id}'
        
class LikeSerializer(NestedHyperlinkedModelSerializer):
    summary = serializers.SerializerMethodField('get_liker')
    object = serializers.SerializerMethodField('get_id_url')
    author = AuthorSerializer(many=False, read_only=True)
    class Meta:
        model = models.Like
        fields = ('summary', 'type', 'author', 'object')

    def get_id_url(self, obj):
        host = self.context['request'].get_host()
        post = obj.post
        comment = obj.comment
        if comment:
            return f'http://{host}/author/{obj.author.id}/posts/{obj.post.id}/comments/{obj.comment.id}'
        elif post:
            return f'http://{host}/author/{obj.author.id}/posts/{obj.post.id}'

    def get_liker(self, obj):
        post = obj.post
        comment = obj.comment
        if comment:
            return obj.author.displayName + " likes your %s" % (comment.type)
        elif post:
            return obj.author.displayName + " likes your %s" % (post.type)
