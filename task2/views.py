from django.shortcuts import render
from django.views.generic import TemplateView

def func(request):
    return render(request, 'func_template.html')


class cls(TemplateView):
    template_name = 'class_template.html'