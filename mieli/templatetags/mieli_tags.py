from django.template import Template, Context
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def render_flatpage(context, flatpage):
    tvalue = Template(flatpage.content)
    return tvalue.render(context)
