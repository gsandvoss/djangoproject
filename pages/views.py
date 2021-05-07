from django.shortcuts import render
from .models import Files
import io
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.http import FileResponse


import mimetypes


def home(request):
	return render(request, "home.html", {})

def about(request):
	from pages.namer import namer
	return render(request, "about.html", {"my_stuff": namer})

def contact(request):
	return render(request, "contact.html", {})

def files(request):
	art_files = Files.objects.all
	return render(request, "art_files.html", {"art_files": art_files})




def download_file(request):
	buffer = io.BytesIO()
	path="art_files/images"
	file_path = os.path.join(settings.STATIC_ROOT,path)
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type=mime_type)
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
	return FileResponse(buffer, as_attachment=True, filename='Chenrezig_Grid.svg')





