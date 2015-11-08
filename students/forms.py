from django import forms
from .models import Alumno_Preparatoria, Alumno_Profesional
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin import widgets

class PreparatoriaForm(forms.ModelForm):
	birth_date = forms.DateField(widget=SelectDateWidget(years = range(1980,2015)))
	graduation_date = forms.DateField(widget=SelectDateWidget())

	def save(self,*args, **kwargs):
		super(PreparatoriaForm, self).save(*args, **kwargs)

	class Meta:
		model = Alumno_Preparatoria
		exclude = ('date_of_registration',)
		# fields
class ProfesionalForm(forms.ModelForm):
	birth_date = forms.DateField(widget=SelectDateWidget(years = range(1980,2015)))

	def save(self,*args, **kwargs):
		super(ProfesionalForm, self).save(*args, **kwargs)

	class Meta:
		model = Alumno_Profesional
		exclude = ('',)
		# fields
