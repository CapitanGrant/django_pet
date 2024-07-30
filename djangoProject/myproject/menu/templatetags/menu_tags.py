from django import template
from django.urls import reverse
from django.db.models import Prefetch

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    path = request.path

    def build_menu_tree(menu_items, parent=None):
        tree = []
        for item in menu_items:
            if item.parent == parent:
                children = build_menu_tree(menu_items, item)
                tree.append({'item': item, 'children': children, 'active': path == item.get_url()})
        return tree

    menu_items = MenuItem.objects.filter(menu_name=menu_name).prefetch_related('children').order_by('parent_id')
    menu_tree = build_menu_tree(menu_items)
    return {'menu_tree': menu_tree}

@register.simple_tag
def resolve_url(item):
    if item.url:
        return item.url
    elif item.named_url:
        try:
            return reverse(item.named_url)
        except:
            return '#'
    return '#'
