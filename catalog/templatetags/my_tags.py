from django import template
from HW19_2.settings import PERMISSIONS_MODERATOR
register = template.Library()

@register.filter
def media_filter(path):
    if path:
        return f'/media/{path}'
    return '#'

@register.filter
def has_moderator_perms(user):
    return all(user.has_perm(f'catalog.{perm[0]}') for perm in PERMISSIONS_MODERATOR)