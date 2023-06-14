from django.urls import path
from django.conf. urls.static import static

from resume_pda import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects', views.projects, name='projects'),
    path('experience', views.experience, name='experience'),
    path('contacts', views.contacts, name='contacts'),
    path('education', views.education, name='education'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
