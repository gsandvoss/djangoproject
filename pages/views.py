from django.shortcuts import render
from .models import Files

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

