from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', include('folio_aws.apps.basic.urls')),
    path('projects/', include('folio_aws.apps.projects.urls')),
    path('admin/', admin.site.urls),
                  # path("favicon.ico",
                  #      RedirectView.as_view(
                  #          url=staticfiles_storage.url("favicon.ico")),
                  #      ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
