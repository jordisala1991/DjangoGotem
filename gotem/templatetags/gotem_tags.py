from django import template
from gotem.models import Sprint

register = template.Library()

@register.inclusion_tag('gotem/sprints-area/sprint-list.html')
def show_sprints(selected_sprint):
    sprints = Sprint.objects.all().order_by('-start_date')
    return { 'selected_sprint' : selected_sprint, 'sprints' : sprints }