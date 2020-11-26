from django import template


register = template.Library()


''' Retorna el nombre del objeto de un Form '''
@register.filter
def modelform_title(modelform):
    return modelform._meta.model._meta.verbose_name.title()
