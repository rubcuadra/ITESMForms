#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
#from django.template.context_processors import csrf
from django.views.generic import View 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Alumno_Preparatoria ,Alumno_Profesional
from sender import MailSender
from . import forms as cForms
from . import constants as c
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
            return redirect('success')
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
            return redirect('success')
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
class SenderView(View):
    template_name='sender.html'
    def get(self, request):
        totalProfe=totalPrepa='?'
        return render(request, self.template_name, locals())

    def post(self, request):
        totalProfe=Alumno_Profesional.objects.count()
        totalPrepa=Alumno_Preparatoria.objects.count()
        if request.POST.get('bttnPreparatoria') or request.POST.get('bttnProfesional'):
            bttn = 3 if request.POST.get('bttnPreparatoria') else 5
            mailer = MailSender(username=c.gmail_username,pwd=c.gmail_pwd,destinatary=c.destinatary,type=bttn)
            topTenAlumnos = Alumno_Preparatoria.objects.all()[:10] if bttn is 3 else Alumno_Profesional.objects.all()[:10]
            csv_report = open('report.csv','w+')
            for alumno in topTenAlumnos:
                csv_report.write(alumno.getCSVLine())
                csv_report.write('\n')
            csv_report.close()
            mailer.attachCSV('report.csv')
            mailer.sendMail()
            del mailer
            for alumno in topTenAlumnos:
                alumno.delete()
                pass
            msg='Envio de alumnos de %s éxitoso!'%('Preparatoria' if bttn is 3 else 'Profesional')
        return render(request, self.template_name, locals())

    def dispatch(self, request, *args, **kwargs):
        return super(SenderView, self).dispatch(request, *args, **kwargs)
def home(request):
    return render(request,'index.html',{})