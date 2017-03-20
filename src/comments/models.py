from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect

# Create your models here.

class CommentManager(models.Manager):
	def all(self):
		qs = super().filter(parent=None)
		return qs

	def filter_by_instance(self, instance):
		content_type = ContentType.objects.get_for_model(instance.__class__)
		obj_id = instance.id
		qs = super().filter(content_type=content_type, object_id=obj_id).filter(parent=None)
		return qs

class Comment(models.Model):
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	content 		= models.TextField()
	timestamp 		= models.DateTimeField(auto_now_add=True)

	content_type 	= models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id 		= models.PositiveIntegerField()
	content_object 	= GenericForeignKey('content_type', 'object_id')
	parent 			= models.ForeignKey("self", null=True, blank=True)

	objects = CommentManager()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return str(self.user.username)

	def get_absolute_url(self):
		return reverse("comments:thread", kwargs={"id": self.id})

	def get_delete_url(self):
		return reverse("comments:delete", kwargs={"id", self.id})

	def children(self):
		return Comment.objects.filter(parent=self)

	@property
	def is_parent(self):
		if self.parent is not None:
			return False
		return True