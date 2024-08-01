
from ..models import Menu
from django import template


register = template.Library()



@register.inclusion_tag('menu/menu_shell.html', takes_context=True)

def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path

    try:
        menu = Menu.objects.get(name=menu_name)
        items = menu.get_items()
    except Menu.DoesNotExist:
        return {'menu': None, 'items': []}



    return {'menu': menu, 'items': items,'current_url':current_url}

