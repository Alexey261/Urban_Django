"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from task4.views import *
from django.views.generic import TemplateView
# from task2.views import func
# from task2.views import МуTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    # path('platform/', platform),
    path('games/', games),
    path('cart/', cart)

    # path('index2/', TemplateView.as_view(template_name='index2.html')),
    # path('func/', func),
    # path('class/', TemplateView.as_view(template_name='class_template.html')),
    # path('class/', МуTemplateView.as_view())

]
