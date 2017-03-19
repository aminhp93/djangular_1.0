from urllib.parse import quote
from django import template

register = template.Library()

@register.filter
def urlify(value):
	return quote(value)