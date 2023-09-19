from django.urls import path
from mainapp import views
from django.views.generic import RedirectView

app_name = 'mainapp'


urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('new_project/', views.NewProjectView.as_view(), name='new_project'),
    path('bad_file/', views.BadFileView.as_view(), name='bad_file'),
    path('files_is_ok/', views.GoodFileView.as_view(), name='files_is_ok'),


    path('', RedirectView.as_view(url='index/'))
]
