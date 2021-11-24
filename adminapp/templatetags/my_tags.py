from django.conf import settings
from django import template

register = template.Library()


@register.filter(name='media_for_products')
def media_for_products(img_path):
    if not img_path:
        img_path = 'products/default.jpg'
    return f'{settings.MEDIA_URL}{img_path}'


# @register.filter(name='media_for_products') -> first way
def media_for_users(img_path):
    if not img_path:
        img_path = 'users_avatar/default_user.jpg'
    return f'{settings.MEDIA_URL}{img_path}'


# register.filter('media_for_products', media_for_products) -> second way
register.filter('media_for_users', media_for_users)
