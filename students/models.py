from django.db import models

# Create your models here.
class Alumno_Preparatoria(models.Model):


	date_Formats = ['%d/%m/%y','%d/%m/%Y']
	prepa_programs = (('PTB','Preparatoria Bilingue'),('PTM','Preparatoria Bicultural'),('IB', 'Preparatoria Internacional'),)

	average = models.DecimalField(max_digits = 4, decimal_places=2,default=75.00 ,verbose_name=u'Promedio de Secundaria')
	name = models.CharField(max_length = 120, verbose_name=u'Nombre')
	last_name = models.CharField(max_length=120, verbose_name=u'Apellidos')
	birth_date = models.DateField(auto_now=False,verbose_name=u'Fecha de Nacimiento')
	nationality = models.CharField(max_length=120,  verbose_name=u'Nacionalidad') 
	high_school = models.CharField(max_length=120,  verbose_name=u'Nombre de Secundaria') 
	graduation_date = models.DateField(auto_now=False,verbose_name=u'Fecha de Graduacion')
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
		return self.name + ' ' + self.last_name

