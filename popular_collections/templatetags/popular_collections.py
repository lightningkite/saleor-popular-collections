from django import template

register = template.Library()


@register.inclusion_tag('popular_collections/dashboard/side_nav_inclusion.html',
                        takes_context=True)
def popular_collections_side_nav(context):
    return context
