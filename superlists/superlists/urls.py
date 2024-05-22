"""
URL configuration for superlists project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
""" Código do Livro -> descontinuado
from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^$', views.home_page, name='home')
]
"""
from django.urls import include, re_path
from lists import views

urlpatterns = [
    re_path(r'^$', views.home_page, name='home')
]

""""alternativa sem regex

from django.urls import include, path
from lists import views

urlpatterns = [
    path('', views.home_page, name='home'),
]
"""



