
from rest_framework.serializers import (
	ModelSerializer, 
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from comments.api.serializers import CommentSerializer
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

post_detail_url = HyperlinkedIdentityField(
        view_name='posts-api:detail',
        lookup_field='slug'
        )

class PostDetailSerializer(ModelSerializer):

	url = post_detail_url
	comments = SerializerMethodField()
	# user = UserDetailSerializer(read_only=True)
	image = SerializerMethodField()
	html = SerializerMethodField()

	class Meta:
		model = Post
		fields = [
			'url',
            'id',
            # 'user',
            'title',
            'slug',
            'content',
            'html',
            'publish',
            'image',
            'comments',

		]

	def get_html(self, obj):
		return obj.get_markdown()

	def get_image(self, obj):
		try:
			image = obj.image.url
		except:
			image = None
		return image

	def get_comments(self, obj):
		print("Hello ")
		c_qs = Comment.objects.filter_by_instance(obj)
		print("hello 2")
		comments = CommentSerializer(c_qs, many=True).data
		print("Hello agian")
		return comments

class PostListSerializer(ModelSerializer):
	user = SerializerMethodField()
	image = SerializerMethodField()
	markdown = SerializerMethodField()

	url = post_detail_url

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
			"slug",
		]



	def get_serializer_context(self):
		return {
			'request': self.request,
			'format': self.format_kwarg,
			'view': self
		}

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