from django.template import Template, Context
from election.models import Election, Option
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def render_flatpage(context, flatpage):
    tvalue = Template(flatpage.content)
    return tvalue.render(context)

@register.inclusion_tag('tags/election_tag.html')
def election(pk):
    e = Election.objects.get(pk=pk)
    return { 'election': e }
