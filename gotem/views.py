from django.shortcuts import render
from django.utils import simplejson as json
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from models import Objective, ObjectiveForm

def index(request):
    return render(request, 'gotem/index.html')

def objective_list(request):
    if request.is_ajax():
        objectives = Objective.objects.all()
        context = { 'objectives' : objectives }
        return render(request, 'gotem/sprint-area/objective-list.html', context)
    else:
        raise Http404

def objective_new(request):
    if request.is_ajax():
        objective_form = ObjectiveForm(request.POST or None)
        if objective_form.is_valid():
            objective_form.save()
            return HttpResponse(json.dumps('success'), mimetype="application/json")
        else:
            return HttpResponseBadRequest(json.dumps(objective_form.errors), mimetype="application/json")
    else:
        raise Http404