from django.shortcuts import render, get_object_or_404
from django.utils import simplejson as json
from django.http import Http404, HttpResponseBadRequest
from models import Objective, Sprint, ObjectiveForm

def index(request):
    
    sprint = Sprint.objects.latest('id')
    return show_sprint(request, sprint.id)

def show_sprint(request, sprint_id):
    
    sprint = get_object_or_404(Sprint, id=sprint_id)
    objectives = Objective.objects.filter(sprint=sprint).order_by('-date')
    form = ObjectiveForm(initial = { 'sprint' : sprint })
    model = { 'sprint' : sprint, 'form' : form, 'objectives' : objectives }
    return render(request, 'gotem/index.html', model)

def objective_new(request):
    
    if request.is_ajax():
        objective_form = ObjectiveForm(request.POST or None)
        if objective_form.is_valid():
            new_objective = objective_form.save()
            return render(request, 'gotem/sprint-area/objective-item.html', { 'objective' : new_objective })
        else:
            return HttpResponseBadRequest(json.dumps(objective_form.errors), mimetype="application/json")
    else:
        raise Http404