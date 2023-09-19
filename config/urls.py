from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainapp/', include('mainapp.urls', namespace='mainapp')),
    path('apiapp/', include('apiapp.urls', namespace='apiapp')),
    path('', RedirectView.as_view(url='mainapp/'))
]
