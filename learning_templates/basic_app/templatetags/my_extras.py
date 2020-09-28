from django import template

register = template.Library()

@register.filter(name='cut') #this code is a decorator
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

#register.filter('cut',cut)