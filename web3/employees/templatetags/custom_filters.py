from django import template

register = template.Library()


@register.filter
def check_day(user_id, day, workdays):
    return any(workday.user.id == user_id and workday.date.day == day for workday in workdays)
