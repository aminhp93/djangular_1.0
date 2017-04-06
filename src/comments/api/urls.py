from django.conf.urls import url

from .views import (
		CommentCreateAPIView,
		CommentListAPIView,
		CommentDetailAPIView,
	)


urlpatterns = [
	url(r'^$', CommentListAPIView.as_view(), name="list"),
	url(r'^create/$', CommentCreateAPIView.as_view(), name='create'),
	url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name="detail"),
	# url(r'^(?P<pk>\d+)/edit/$', CommentEditAPIView.as_view(), name="edit"),
	# url(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name="update"),
	# url(r'^(?P<slug>[\w-]+)/delete/$', PostDeleteAPIView.as_view(), name="delete"),
]