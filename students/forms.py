from django import forms
from .models import Alumno_Preparatoria
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin import widgets

class PreparatoriaForm(forms.ModelForm):
	birth_date = forms.DateField(widget=SelectDateWidget(years = range(1980,2015)))
	graduation_date = forms.DateField(widget=widgets.AdminDateWidget())
	

	def save(self,*args, **kwargs):
		super(PreparatoriaForm, self).save(*args, **kwargs)

	class Meta:
		model = Alumno_Preparatoria
		
		exclude = ('',)
		# fields

