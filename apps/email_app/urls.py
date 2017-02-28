from django.conf.urls import url

from . import views

urlpatterns =[
	url(r'^validate/success/delete/(?P<id>\d+)$', views.delete, name='email_delete'),
	url(r'^validate/success$', views.success, name='email_valid'),
	url(r'^validate$', views.process, name='email_check'),
	url(r'^email$', views.index, name='email_index'),
]
