from django.conf.urls import url

from .views import (
	demo_slide_show,
	slide_show_pictures,
	)

app_name='demo'

urlpatterns = [
	url(r'^slideshow/$', demo_slide_show, name='slideshow'),
	url(r'^images/$', slide_show_pictures, name='images'),
]

