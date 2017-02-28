"""integration_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

urlpatterns = [
	url(r'^ninja/', include('apps.ninja_app.urls', namespace='disappear')),
	url(r'^gold/', include('apps.gold_app.urls', namespace='ninja_gold')),
	url(r'^email/', include('apps.email_app.urls', namespace='email_validate')),
	url(r'^course/', include('apps.course_app.urls', namespace='courses')),
	url(r'^', include('apps.login_reg_app.urls', namespace='login_reg')),
]
