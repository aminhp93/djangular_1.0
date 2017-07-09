"""djangular URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from rest_framework_jwt.views import obtain_jwt_token

from ang.views import AngularTemplateView

from accounts.views import (login_view, register_view, logout_view)
from posts import views as posts_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', posts_views.post_list),
    url(r'^login/', login_view, name="login"),
    url(r'^logout/', logout_view, name="logout"),
    url(r'^register/', register_view, name="register"),
    url(r'^', include("posts.urls", namespace="posts")),
    url(r'^api/auth/token/', obtain_jwt_token),
    url(r'^api/posts/', include("posts.api.urls", namespace="posts-api")),
    url(r'^api/users/', include("accounts.api.urls", namespace="users-api")),
    url(r'^api/comments/', include("comments.api.urls", namespace="comments-api")),
    url(r'^api/templates/(?P<item>[A-Za-z0-9\_\-\.\/]+)\.html$', AngularTemplateView.as_view()),
    url(r'^comments/', include("comments.urls", namespace="comments")),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'', TemplateView.as_view(template_name="ang/home.html")),
]