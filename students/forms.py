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
		exclude = ('',)
		# fields
class ProfesionalForm(forms.ModelForm):
	options= (
		('ITC', 'Ingenieria en Tecnologias Computacionales'),
		('IMT','Ingenieria en Mecatronica'),
		('IDS', 'Ingenieria en Desarollo Sustentable'),
		('IMI', 'Ingenieria en Produccion Musical y Digital'),)

	birth_date = forms.DateField(widget=SelectDateWidget(years = range(1980,2015)))
	interests = forms.MultipleChoiceField(choices = options,widget=forms.CheckboxSelectMultiple())

	def save(self,*args, **kwargs):
		super(ProfesionalForm, self).save(*args, **kwargs)

	class Meta:
		model = Alumno_Profesional
		exclude = ('',)
		# fields
