import importlib

from django import template

from saleor.product.models import Collection

register = template.Library()

PopularCollection = importlib.import_module(
    "saleor-popular-collections.popular_collections.models").PopularCollection


@register.inclusion_tag(
    'popular_collections/dashboard/side_nav_inclusion.html',
    takes_context=True)
def popular_collections_side_nav(context):
    return context


@register.inclusion_tag('includes/popular_collections.html')
def popular_collections(super_collection=None):
    collections = Collection.objects.filter(popular__isnull=False)
    if super_collection:
        for c in collections:
            if super_collection not in c.super_collections.all():
                collections = collections.exclude(id=c.id)
    # collections = collections[0:6]
    return {"collections": collections}
