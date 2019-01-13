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

def manifest_json(request):
	response = {
		  "short_name": "Maps",
		  "name": "Google Maps",
		  "icons": [
		    {
		      "src": "/static/demo/slideshow/images/icons-240.png",
		      "type": "image/png",
		      "sizes": "240x240"
		    },
		    {
		      "src": "/static/demo/slideshow/images/icons-512.png",
		      "type": "image/png",
		      "sizes": "512x512"
		    }
		  ],
		  "start_url": "/demo/slideshow/?source=pwa",
		  "background_color": "#3367D6",
		  "display": "standalone",
		  "scope": "/",
		  "theme_color": "#3367D6"
		}

	return JsonResponse(response)
