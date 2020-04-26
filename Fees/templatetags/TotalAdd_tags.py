from django import template

register = template.Library()

# @register.filter
# def TotalAdds():
    
#     return 0

@register.filter
def TotalAdd(value,arg):
    
    return value + arg
    