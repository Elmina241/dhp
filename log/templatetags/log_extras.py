from django import template

register = template.Library()

@register.filter(name='sort')
def listsort(value):
    if isinstance(value, dict):
        a = []
        key_list = reversed(sorted(value.keys()))
        for key in key_list:
            a.append((key, value[key]))
        return a
    elif isinstance(value, list):
        return sorted(value)
    else:
        return value

listsort.is_safe = True