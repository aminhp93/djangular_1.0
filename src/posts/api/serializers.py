from rest_framework.serializers import (
	ModelSerializer, 
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from comments.api.serializers import CommentListSerializer
from comments.models import Comment

from posts.models import Post

class PostCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			# "id",
			"title",
			# "slug",
			"content",
			"publish",
		]

class PostDetailSerializer(ModelSerializer):
	comments = SerializerMethodField()
	class Meta:
		model = Post
		fields = [
			"id",
			"title",
			"slug",
			"content",
			"publish",
			"comments"
		]

	def get_comments(self, obj):
		c_qs = Comment.objects.filter_by_instance(obj)
		comments = CommentSerializer(c_qs, many=True).data
		return comments

class PostListSerializer(ModelSerializer):
	user = SerializerMethodField()
	image = SerializerMethodField()
	markdown = SerializerMethodField()

	url = HyperlinkedIdentityField(
			view_name='posts-api:detail',
			lookup_field='slug',
		)

	class Meta:
		model = Post
		fields = [
			"url",
			'user',
			"id",
			"title",
			"content",
			"publish",
			"image",
			"markdown",
		]

	def get_user(self, obj):
		return str(obj.user.username)

	def get_image(self, obj):
		try:
			image = obj.image.url
		except:
			image = None
		return image

	def get_markdown(self, obj):
		return obj.get_markdown()