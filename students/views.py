from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
#from django.template.context_processors import csrf
from .models import Alumno_Preparatoria
from django.views.generic import View 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms as cForms
# Create your views here.

class PrepaView(View):
    template_name = 'preparatoria.html'
    def get(self, request):
        form = cForms.PreparatoriaForm()
        return render(request, self.template_name, locals())

    def post(self, request):
        form = cForms.PreparatoriaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, self.template_name, locals())

    def dispatch(self, request, *args, **kwargs):
        return super(PrepaView, self).dispatch(request, *args, **kwargs)

class ProfeView(View):
    template_name='profesional.html'
    def get(self, request):
        form = cForms.ProfesionalForm()
        return render(request, self.template_name, locals())

    def post(self, request):
        form = cForms.ProfesionalForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, self.template_name, locals())

    def dispatch(self, request, *args, **kwargs):
        return super(ProfeView, self).dispatch(request, *args, **kwargs)
class SuccessView(View):
    template_name='success.html'
    def get(self, request):
        return render(request, self.template_name, locals())

    def post(self, request):
        return render(request, self.template_name, locals())

    def dispatch(self, request, *args, **kwargs):
        return super(SuccessView, self).dispatch(request, *args, **kwargs)

def home(request):
    return render(
        request,
        'index.html',
        {}
    )