
from django.shortcuts import render
from django.views import generic
from .models import Summary, NavBarButton


class SummaryView(generic.ListView):
    template_name = 'basic/home_index.html'
    context_object_name = 'summary_list'

    def get_queryset(self):
        return Summary.objects.all()


class NavBarView(generic.ListView):
    template_name = 'basic/navbar.html'
    context_object_name = 'navbar_buttons'

    def get_queryset(self):
        return NavBarButton.objects.all()


def contact(request):
    return render(request, 'basic/contact_index.html')