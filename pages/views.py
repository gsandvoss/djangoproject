from django.shortcuts import render
from .models import Files

import os
from django.conf import settings
from django.http import HttpResponse, Http404

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
    # fill these variables with real value
    path = "/downloads"
    os.chmod("downloads/Sitting_Buddha.svg", 0o777)
    fl_path = ("/downloads")
    filename = "Sitting_Buddha.svg"
    fl = open(fl_path, 'w')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s * %s"
    return response


def download(request, path):

    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type=mime_type)
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404