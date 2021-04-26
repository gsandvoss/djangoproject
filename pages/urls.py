
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
	path('', views.home, name = 'home'),
	path('about/', views.about, name = 'about'),
	path('contact/', views.contact, name = 'contact'),
	path('art_files/', views.files, name = 'art files'),
	path('static', views.download_file, name = 'download'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)