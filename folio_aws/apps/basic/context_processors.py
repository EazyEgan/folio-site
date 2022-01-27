from .models import NavBarButton


def navbar_processor(request):
    return {
        'navbar_buttons': NavBarButton.objects.all()
    }
