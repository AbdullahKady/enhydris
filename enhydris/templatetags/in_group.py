from django import template

register = template.Library()


@register.filter
def in_group(user, group):
    """Returns True/False if the user is in the given group(s).
    Usage::
        {% if user|in_group:"Friends" %}
        or
        {% if user|in_group:"Friends,Enemies" %}
        ...
        {% endif %}
    You can specify a single group or comma-delimited list.
    No white space allowed.
    """
    import re

    if re.search(",", group):
        group_list = re.sub(r"\s+", "", group).split(",")
    elif re.search(" ", group):
        group_list = group.split()
    else:
        group_list = [group]
    user_groups = []
    for group in user.groups.all():
        user_groups.append(str(group.name))
    if [x for x in group_list if x in user_groups]:
        return True
    else:
        return False


in_group.is_safe = True