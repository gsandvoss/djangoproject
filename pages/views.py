from django.shortcuts import render
from .models import Files

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
    # fill these variables with real values
    fl_path = "static/images"
    filename = "Sitting_Buddha.svg"

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response