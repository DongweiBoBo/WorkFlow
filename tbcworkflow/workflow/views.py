from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import *


def index(request):
    projects = Project.objects.all()
    return render(request, 'workflow/index.html',{'projects':projects})

def detail(request, project_id):
    project = Project.objects.get(pk=project_id)
    samples = Sample.objects.filter(project_id=project_id)
    sequences = Sequence.objects.filter(project_id=project_id)
    assemblys = Assembly.objects.filter(project_id=project_id)
    genemodels = Genemodel.objects.filter(project_id=project_id)
    analyses = Analyse.objects.filter(project_id=project_id)
    return render(request, 'workflow/detail.html', {'project':project,
        'samples':samples,
        'sequences':sequences,
        'assemblys':assemblys,
        'genemodels':genemodels,
        'analyses':analyses
    })

