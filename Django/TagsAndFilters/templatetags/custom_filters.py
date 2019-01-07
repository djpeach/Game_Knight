from django import template
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.filter(name='is_first')
def is_first(counter, text):
	return text if counter == 1 else ''

