from django.db.models import Q
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post

def post_list(request):
	queryset_list = Post.objects.active()
	 # Show 25 contacts per page

	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.all()

	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query) |
			Q(content__icontains=query) | 
			Q(user__first_name__icontains=query)
			).distinct()

	paginator = Paginator(queryset_list, 25)

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,
	}

	return render(request, "post_list.html", context)

def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	form = PostForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Success")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Error")

	context = {
		"form": form
	}
	return render(request, "post_form.html", context)

def post_detail(request, id=None):

	instance = get_object_or_404(Post, id=id)
	if instance.draft or instance.publish > timezone.now().date():
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	context = {
		"instance": instance,
	}	
	return render(request, "post_detail.html", context)

def post_update(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Saved", extra_tags="some-tag")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Error")

	context = {
		"instance": instance,
		"form": form,
	}	
	return render(request, "post_form.html", context)
def post_delete(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Successfully deleted")

	return redirect("posts:list")
