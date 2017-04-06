from django.shortcuts import render

def get_angular_template(request, path=None):
	template = "ang/app/blog_list.html"
	context = {

	}
	return render(request, template, context)