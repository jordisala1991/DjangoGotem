from django import template
from gotem.models import ObjectiveForm

register = template.Library()

@register.inclusion_tag('gotem/sprint-area/objective-list__controls.html')
def objective_form():
	form = ObjectiveForm()
	return { 'form' : form }