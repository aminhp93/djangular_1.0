from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.post_list, name="list"),
	url(r'^create/$', views.post_create),
	url(r'^(?P<slug>[\w-]+)/$', views.post_detail, name="detail"),
	url(r'^(?P<slug>[\w-]+)/edit/$', views.post_update, name="update"),
	url(r'^(?P<slug>[\w-]+)/delete/$', views.post_delete, name="delete"),
]