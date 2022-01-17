from django.shortcuts import render
from django.views import generic
from .models import Project
from django.db.models import Q

class IndexView(generic.ListView):
    template_name = 'projects/index.html'
    context_object_name = 'project_list'


    def get_queryset(self):
        query = self.request.GET.get('lang')
        #print(query)
        if query:

            q = Q()
            q |= Q(languages__icontains=query)
            return Project.objects.filter(q)

        return Project.objects.all()


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/home_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'projects/detail.html', context)
