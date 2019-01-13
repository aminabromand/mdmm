from django.http import JsonResponse
from django.shortcuts import render

from .models import SlideshowSlide

# Create your views here.

def demo_slide_show(request):
	context = {
		'title':'About Page',
		'content': 'Welcome to the about page.'
	}
	return render(request, 'demo/demo.html', context)


def slide_show_pictures(request):
	qs = SlideshowSlide.objects.only('image')
	images = []
	for slide in qs:
		images.append(slide.image.url)
	response = {'images': images}
	return JsonResponse(response)
