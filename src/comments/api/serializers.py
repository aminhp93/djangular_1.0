from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from rest_framework import serializers

from rest_framework.serializers import (
	ModelSerializer, 
	HyperlinkedIdentityField,
	SerializerMethodField,
	ValidationError,
	)

from comments.models import Comment

from accounts.api.serializers import UserDetailSerializer

User = get_user_model()

# def create_comment_serializer(model_type='post', slug=None, parent_id=None, user=None):
class CommentCreateSerializer(ModelSerializer):

	type = serializers.CharField(required=False, write_only=True)
	slug = serializers.SlugField(write_only=True)
	parent_id = serializers.IntegerField(required=False)

	class Meta:
		model = Comment
		fields = [
			"id",
			"content",
			"type",
			"slug",
			"parent_id",
			"timestamp",

		]

	# def __init__(self, *args, **kwargs):
	# 	self.model_type = model_type
	# 	self.slug = slug
	# 	self.parent_obj = None

	# 	if parent_id:
	# 		parent_qs = Comment.objects.filter(id=parent_id)
	# 		if parent_qs.exists() and parent_qs.count() == 1:
	# 			self.parent_obj = parent_qs.first()
	# 	return super().__init__(*args, **kwargs)

	def validate(self, data):
		# model_type = self.model_type
		model_type = data.get("type", "post")

		model_qs = ContentType.objects.filter(model=model_type)
		if not model_qs.exists() or model_qs.count() != 1:
			raise ValidationError("This is not valid content type")
		SomeModel = model_qs.first().model_class()
		slug = data.get("slug")
		obj_qs = SomeModel.objects.filter(slug=slug)
		if not obj_qs.exists() or obj_qs.count() != 1:
			raise ValidationError("This is not a slug for this content")
		print("WOOOOOOOO")
		parent_id = data.get("parent_id")
		if parent_id:
			parent_qs = Comment.objects.filter(id=parent_id)
			if not parent_qs.exists() or parent_qs.count() != 1:
				raise ValidationError("This is not a valid parent for this content")
		return data

	def create(self, validated_data):
		content = validated_data.get("content")
		# if user and user.is_anonymous() == False:
			
		# 	main_user = user
		# else:
		# 	main_user = User.objects.all().first()
		# model_type = self.model_type
		# slug = self.slug
		# parent_obj = self.parent_obj

		model_type 	= validated_data.get("type", "post")
		slug 		= validated_data.get("slug")
		parent_id  	= validated_data.get("parent_id")

		parent_obj = None
		if parent_id:
			parent_obj = Comment.objects.filter(id=parent_id).first()

		user = self.context["user"]
		print(user)
		
		comment = Comment.objects.create_by_model_type(
			model_type,
			slug,
			content,
			user,
			parent_obj=parent_obj,
			)

		return comment

	# return CommentCreateSerializer

class CommentSerializer(ModelSerializer):
    reply_count = SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            'id',
            'content_type',
            'object_id',
            'parent',
            'content',
            'reply_count',
            'timestamp',
        ]
    
    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0

class CommentListSerializer(ModelSerializer):
	url = HyperlinkedIdentityField(
			view_name='comments-api:detail',
		)

	reply_count = SerializerMethodField()
	class Meta:
		model = Comment
		fields = [
			"url",
			"id",
			# "content_type",
			# "object_id",
			# "parent",
			"content",
			"reply_count",
			"timestamp",
		]

	def get_reply_count(self, obj):
		if obj.is_parent:
			return obj.children().count()
		return 0

class CommentChildSerializer(ModelSerializer):
	user = UserDetailSerializer()
	class Meta:
		model = Comment
		fields = [
			"id",
			"user",
			"content",
			"timestamp",
		]


class CommentDetailSerializer(ModelSerializer):
	user = UserDetailSerializer()
	content_object_url = SerializerMethodField()
	replies = SerializerMethodField()
	class Meta:
		model = Comment
		fields = [
			"id",
			"user",
			"content_type",
			"object_id",
			"content",
			"replies",
			"content_object_url",
		]
		read_only_fields = [
			# 'content_type',
			'reply_count',
			'replies',
			# 'object_id',
		]

	def get_replies(self, obj):
		if obj.is_parent:
			return CommentChildSerializer(obj.children(), many=True).data
		return None

	def get_content_object_url(self, obj):
		try:
			return obj.content_object.get_api_url()
		except:
			return None

# class CommentEditSerializer(ModelSerializer):
# 	class Meta:
# 		model = Comment
# 		fields = [
# 			"id",
# 			"content",
# 		]
