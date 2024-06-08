from django import template

register = template.Library()

@register.filter
def truncatechars(value, arg):
    """
    Обрезает строку после определенного количества символов.
    Аргумент: Количество символов, после которого строка будет обрезана.
    """
    try:
        length = int(arg)
    except ValueError:
        return value  # Неправильный аргумент, вернуть оригинальную строку
    if len(value) > length:
        return value[:length] + '...'
    return value