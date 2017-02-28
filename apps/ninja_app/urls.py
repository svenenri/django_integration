from django.conf.urls import url, include
from . import views
urlpatterns = [
	url(r'^ninjas/(?P<color>[a-z A-Z]+)$', views.color, name='get_color'),
	url(r'^ninjas$', views.ninjas, name='ninjas_all'),
    url(r'^index$', views.index, name='ninjas_view'),
]
