from django import template
from ..models import Asset, Software

register = template.Library()


@register.simple_tag
def get_recent_asset(num=6):
    asset = Asset.objects.filter()[:num]
    return asset


@register.simple_tag
def get_recent_software(num=6):
    software = Software.objects.filter()[:num]
    return software

