from django import template

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

@register.filter(name='has_any_group')
def has_any_group(user, groups):
    groups = groups.split(',')
    print(groups)
    return(any(group in [group.name for group in user.groups.filter(name=group)] for group in groups))