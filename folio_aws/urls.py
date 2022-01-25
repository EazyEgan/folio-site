from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('folio_aws.apps.basic.urls')),
    path('projects/', include('folio_aws.apps.projects.urls')),
    path('admin/login/', auth_views.LoginView.as_view(
                      template_name='admin/login.html'), name='login'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
