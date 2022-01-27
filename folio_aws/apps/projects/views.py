from django.shortcuts import render
from django.views import generic
from .models import Project
from django.db.models import Q


class IndexView(generic.ListView):
    template_name = 'projects/index.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        query = self.request.GET.get('lang')
        if query:
            q = Q()
            q |= Q(languages__icontains=query)
            return Project.objects.filter(q)

        return Project.objects.all()

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'projects/detail.html', context)

"""
class DetailView(generic.DetailView):
    model = Question
    template_name = 'yourApp/detail.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

"""