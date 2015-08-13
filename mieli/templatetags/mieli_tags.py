from django.template import Template
from election.models import Election
from mieli.api import nexus
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def render_flatpage(context, flatpage):
    tvalue = Template(flatpage.content)
    return tvalue.render(context)

@register.inclusion_tag('tags/election_tag.html')
def election(pk, only_button=False):
    e = Election.objects.get(pk=pk)
    return { 'election': e, 'only_button': only_button }

@register.inclusion_tag('tags/election_tag.html', takes_context=True)
def geo_election(context, only_button=False):
    request = context['request']
    user = request.user
    try:
        location = user.location_set.get()
        nexus_ = nexus.get(name=location.admin2.name.split(' ')[-1], organization=request.organization)
        e = Election.objects.get(nexus=nexus_, active=True)
    except:
        e = None
    return { 'election': e, 'only_button': only_button }
