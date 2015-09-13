from django.db import models
from django.core.exceptions import ValidationError

def validate_length(value,length=24):
	print len(str(value))
	if len(str(value)) != length:
		raise ValidationError('Debes elegir 3 opciones')
def validate_year(value,length =4):
	if len(str(value)) != length:
		print len(str(value))
		raise ValidationError('Year is Incorrect')




date_Formats = ['%d/%m/%y','%d/%m/%Y']
# Create your models here.
class Alumno_Preparatoria(models.Model):
	prepa_programs = (('PTB','Preparatoria Bilingue'),('PTM','Preparatoria Bicultural'),('IB', 'Preparatoria Internacional'),)
	#FECHA DE CUANDO SE REALIZA 
	average = models.DecimalField(max_digits = 4, decimal_places=2,default=75.00 ,verbose_name=u'Promedio de Secundaria')
	name = models.CharField(max_length = 120, verbose_name=u'Nombre y Apellidos')
	birth_date = models.DateField(auto_now=False,verbose_name=u'Fecha de Nacimiento')
	nationality = models.CharField(max_length=120,  verbose_name=u'Nacionalidad') 
	high_school = models.CharField(max_length=120,  verbose_name=u'Nombre de Secundaria') 
	graduation_date = models.DateField(auto_now=False,verbose_name=u'Fecha de Graduacion ')
	phone_number = models.CharField(max_length=10, verbose_name=u'TelCasa')
	cellphone_number = models.CharField(max_length=10, verbose_name=u'Celular')
	email = models.EmailField(verbose_name=u'Mail')
	street_and_number = models.CharField(max_length=200, verbose_name=u'Calle y Numero')
	district_and_zipcode = models.CharField(max_length=200,verbose_name=u'Colonia y C.P')
	city_and_county = models.CharField(max_length=200, verbose_name=u'Ciudad y Estado')
	father_name = models.CharField(max_length = 120, verbose_name=u'Nombre de Padre')
	mother_name = models.CharField(max_length = 120, verbose_name=u'Nombre de Madre')
	program = models.CharField(max_length=3, choices=prepa_programs,verbose_name=u'Programa Academico: ')
	exam_done = models.CharField(max_length=2, choices=(('Si','Si'),('No','No')), default='No',verbose_name=u'Ya presentaste examen?')

	def __unicode__(self):
		return self.name 

class Alumno_Profesional(models.Model):

	fechas_Ingreso = (('AD','Agosto-Diciembre'),('EM','Enero-Mayo'))
	complete_name = models.CharField(max_length = 120, verbose_name=u'Nombre y Apellidos')
	birth_date = models.DateField(auto_now=False,verbose_name=u'Fecha de Nacimiento')
	phone_number = models.CharField(max_length=10, verbose_name=u'TelCasa')
	cellphone_number = models.CharField(max_length=10, verbose_name=u'Celular')
	email = models.EmailField(verbose_name=u'Mail')
	facebook = models.CharField(max_length = 120, verbose_name=u'Facebook: ')
	twitter = models.CharField(max_length = 120, verbose_name=u'Twitter')
	high_school = models.CharField(max_length=120,  verbose_name=u'Nombre de Preparatoria') 
	average = models.DecimalField(max_digits = 4, decimal_places=2,default=75.00 ,verbose_name=u'Promedio de Preparatoria')
	interests = models.CharField(validators=[validate_length],max_length=130,verbose_name=u'Carreras de Interes')
	starting_date = models.CharField(max_length=2, choices=fechas_Ingreso,verbose_name=u'Periodo de Ingreso')
	starting_year = models.IntegerField(validators=[validate_year],default=2015,verbose_name=u'Year de Ingreso')
	
	def __unicode__(self):
		return self.complete_name

