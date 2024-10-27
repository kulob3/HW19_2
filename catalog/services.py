from django.conf import settings
from django.core.cache import cache

from catalog.models import Product

CACHE_ENABLED = settings.CACHE_ENABLED

def get_product_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'product'
    product = cache.get(key)
    if product is not None:
        return product
    product = Product.objects.all()
    cache.set(key, product)
    return product

def get_category_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.values('category').distinct()
    key = 'categories'
    categories = cache.get(key)
    if categories is not None:
        return categories
    categories = Product.objects.values('category').distinct()
    cache.set(key, categories)
    return categories

