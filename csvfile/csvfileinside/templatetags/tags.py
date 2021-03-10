from django.template import Library
from django.core.serializers import serialize


register = Library()

@register.filter
def json(queryset):
    return serialize('json', queryset)