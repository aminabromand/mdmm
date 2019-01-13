from django.conf.urls import url

from .views import (
	demo_slide_show,
	slide_show_pictures,
	manifest_json,
	)

app_name='demo'

urlpatterns = [
	url(r'^slideshow/$', demo_slide_show, name='slideshow'),
	url(r'^images/$', slide_show_pictures, name='images'),
	url(r'^slideshow/manifest.json$', manifest_json, name='manifest'),
]

