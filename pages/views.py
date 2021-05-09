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
	path_01="art_files/images/Chenrezig_Grid.svg"
	path_02 = os.path.join(path_01)
	get_file = open(path_02, 'rb')
	return FileResponse(get_file, as_attachment=True)




