from django.db import models
from django.core.exceptions import ValidationError
import catalogs as c

def validate_length(value,length=24):
	print len(str(value))
	if len(str(value)) != length:
		raise ValidationError('Debes elegir 3 opciones')
def validate_year(value,length =4):
	if len(str(value)) != length:
		print len(str(value))
		raise ValidationError('Year is Incorrect')

date_Formats = ['%d/%m/%y','%d/%m/%Y']
class Alumno_Preparatoria(models.Model):
	date_of_registration=models.DateField(auto_now=True,verbose_name=u'Fecha De Registro')
	first_time = models.BooleanField(default=True,verbose_name=u'Ya habias estado en algun Tec?')
	average = models.DecimalField(max_digits = 4, decimal_places=2,default=75.00 ,verbose_name=u'Promedio de Secundaria')
	name = models.CharField(max_length = 120, verbose_name=u'Nombre(s)')
	paternal_last_name=models.CharField(max_length = 120, verbose_name=u'Apellido Paterno')
	maternal_last_name=models.CharField(max_length = 120, verbose_name=u'Apellido Materno',blank=True)
	gender = models.CharField(max_length=1, choices=c.gen,verbose_name=u'Sexo: ')
	birth_date = models.DateField(auto_now=False,verbose_name=u'Fecha de Nacimiento')
	nationality = models.CharField(max_length=120,  verbose_name=u'Nacionalidad',blank=True) 
	high_school = models.CharField(max_length=120, choices=c.escuelas,  verbose_name=u'Nombre de Secundaria') 
	graduation_date = models.DateField(auto_now=False,verbose_name=u'Fecha de Graduacion ',blank=True)
	lada_phone_number = models.CharField(max_length=3,verbose_name=u'Lada de Telefono de Casa',help_text='DF = 55')
	phone_number = models.CharField(max_length=8, verbose_name=u'Telefono de Casa')
	cellphone_number = models.CharField(max_length=10, verbose_name=u'Celular',blank=True)
	email = models.EmailField(verbose_name=u'Mail')
	street_and_number = models.CharField(max_length=200, verbose_name=u'Calle y Numero',blank=True)
	district = models.CharField(max_length=200,verbose_name=u'Colonia',blank=True)
	zipcode = models.CharField(max_length=10,verbose_name=u'C.P.',blank=True)
	city_and_county = models.CharField(max_length=200, verbose_name=u'Ciudad y Estado',blank=True)
	father_name = models.CharField(max_length = 120, verbose_name=u'Nombre de Padre',blank=True)
	mother_name = models.CharField(max_length = 120, verbose_name=u'Nombre de Madre',blank=True)
	program = models.CharField(max_length=3, choices=c.prepa_programs,verbose_name=u'Programa Academico: ')
	period = models.CharField(max_length=6, choices=c.periodos,verbose_name=u'Periodo: ')
	exam_done = models.CharField(max_length=2, choices=(('Si','Si'),('No','No')), default='No',verbose_name=u'Ya presentaste examen?')
	def getCSVLine(s):
		params = (2, #CAMPUS
			3, #NIVEL PREPARATORIA
			1, #SESION PRESENCIAL
			s.period, 
			s.program, 
			'',#Programa 2
			'',#Programa 3
			s.name,
			s.paternal_last_name,
			s.maternal_last_name,
			s.birth_date,
			'',#Clave Pais Nacimiento
			'',#Clave Estado Nacimiento
			'',#Clave Municipio Nacimiento
			'',#Clave Ciudad Nacimiento
			'',#Clave Nacionalidad
			s.street_and_number,
			s.district,#Clave Colonia
			s.zipcode,
			'',#Clave Pais 
			'',#Clave Estado 
			'',#Clave Municipio 
			'',#Clave Ciudad 
			'', #Clave int. Tel
			s.lada_phone_number,#Lada Tel
			s.phone_number,
			'',#Clave int. Cel
			'',#Lada Cel
			s.cellphone_number,
			s.email,
			'',#Insititucion Educativa 1
			'',#Insititucion Educativa 2
			'',#Insititucion Educativa 3
			'',#Comentario +
			'',#Clave origen 2
			s.high_school,#Clave Escuela Procedencia +
			s.average,
			s.graduation_date,#Fecha Esperada Graduacion 
			'PIS' if s.first_time else 'PIN',#Ingreso, Primer_Ingreso_Nivel
			'',#Padre Titulo Trato
			'',#Padre Fallecido
			s.father_name,#Padre Nombre
			'',#Padre Ap.Paterno
			'',#Padre Ap.Materno
			'',#Padre Correo
			'',#Padre Clave int. 
			'',#Padre Lada 
			'',#Padre Tel .
			'',#Padre Ext. 
			'',#Madre Titulo Trato
			'',#Madre Fallecido
			s.mother_name,#Madre Nombre
			'',#Madre Ap. Paterno
			'',#Madre Ap. Materno
			'',#Madre Correo
			'',#Madre Clave int. 
			'',#Madre Lada 
			'',#Madre Tel .
			'',#Madre Ext. 
			'',#Tutor Titulo Trato
			'',#Tutor Fallecido
			'',#Tutor Nombre
			'',#Tutor Ap. Paterno
			'',#Tutor Ap. Materno
			'',#Tutor Correo
			'',#Tutor Clave int.
			'',#Tutor Lada 	
			'',#Tutor Tel .					
			'',#Tutor Ext.
			'',#Clave Semaforo
			'',#Titulado
			'',#Cedula Profesional
			'',#Clave int. Oficina
			'',#Lada oficina
			'',#Tel . Oficina
			'',#Ext. Oficina
			'',#Radio
			'',#Clave Radio
			'',#Correo laboral
			'',#Empresa	
			'',#Giro
			'',#Puesto
			'',#Area
			'',)#Hora de Contacto
		return '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s'%(params[0],params[1],params[2],params[3],params[4],params[5],params[6],params[7],params[8],params[9],params[10],params[11],params[12],params[13],params[14],params[15],params[16],params[17],params[18],params[19],params[20],params[21],params[22],params[23],params[24],params[25],params[26],params[27],params[28],params[29],params[30],params[31],params[32],params[33],params[34],params[35],params[36],params[37],params[38],params[39],params[40],params[41],params[42],params[43],params[44],params[45],params[46],params[47],params[48],params[49],params[50],params[51],params[52],params[53],params[54],params[55],params[56],params[57],params[58],params[59],params[60],params[61],params[62],params[63],params[64],params[65],params[66],params[67],params[68],params[69],params[70],params[71],params[72],params[73],params[74],params[75],params[76],params[77],params[78],params[79],params[80],params[81],params[82],params[83])
	def __unicode__(self):
		return self.name 

class Alumno_Profesional(models.Model):
	date_of_registration=models.DateField(auto_now=True,verbose_name=u'Fecha De Registro')
	first_time = models.BooleanField(default=True,verbose_name=u'Ya habias estado en algun Tec?')
	average = models.DecimalField(max_digits = 4, decimal_places=2,default=75.00 ,verbose_name=u'Promedio de Preparatoria')
	name = models.CharField(max_length = 120, verbose_name=u'Nombre(s)')
	paternal_last_name=models.CharField(max_length = 120, verbose_name=u'Apellido Paterno')
	maternal_last_name=models.CharField(max_length = 120, verbose_name=u'Apellido Materno',blank=True)
	gender = models.CharField(max_length=1, choices=c.gen,verbose_name=u'Sexo: ')
	birth_date = models.DateField(auto_now=False,verbose_name=u'Fecha de Nacimiento')
	nationality = models.CharField(max_length=120,  verbose_name=u'Nacionalidad',blank=True) 
	lada_phone_number = models.CharField(max_length=3,verbose_name=u'Lada de Telefono de Casa',help_text='DF = 55')
	phone_number = models.CharField(max_length=8, verbose_name=u'Telefono de Casa')
	cellphone_number = models.CharField(max_length=10, verbose_name=u'Celular',blank=True)
	email = models.EmailField(verbose_name=u'Mail')
	street_and_number = models.CharField(max_length=200, verbose_name=u'Calle y Numero',blank=True)
	district = models.CharField(max_length=200,verbose_name=u'Colonia',blank=True)
	zipcode = models.CharField(max_length=10,verbose_name=u'C.P.',blank=True)
	city_and_county = models.CharField(max_length=200, verbose_name=u'Ciudad y Estado',blank=True)
	father_name = models.CharField(max_length = 120, verbose_name=u'Nombre de Padre',blank=True)
	mother_name = models.CharField(max_length = 120, verbose_name=u'Nombre de Madre',blank=True)
	period = models.CharField(max_length=6, choices=c.periodos,verbose_name=u'Periodo: ')
	facebook = models.CharField(max_length = 120, verbose_name=u'Facebook: ')
	twitter = models.CharField(max_length = 120, verbose_name=u'Twitter')
	prev_school = models.CharField(max_length=120,choices=c.universidades, verbose_name=u'Nombre de Preparatoria') 
	program = models.CharField(max_length=3, choices=c.carreras,verbose_name=u'Carrera de interes:',default='')
	program2 = models.CharField(max_length=3, choices=c.carreras,verbose_name=u'Carrera de interes 2:',blank=True)
	program3 = models.CharField(max_length=3, choices=c.carreras,verbose_name=u'Carrera de interes 3:',blank=True)
	
	def getCSVLine(s):
		params = (2, #CAMPUS
			5, #NIVEL PREPARATORIA
			1, #SESION PRESENCIAL
			s.period, 
			s.program, 
			s.program2,#Programa 2
			s.program3,#Programa 3
			s.name,
			s.paternal_last_name,
			s.maternal_last_name,
			s.birth_date,
			'',#Clave Pais Nacimiento
			'',#Clave Estado Nacimiento
			'',#Clave Municipio Nacimiento
			'',#Clave Ciudad Nacimiento
			'',#Clave Nacionalidad
			s.street_and_number,
			s.district,#Clave Colonia
			s.zipcode,
			'',#Clave Pais 
			'',#Clave Estado 
			'',#Clave Municipio 
			'',#Clave Ciudad 
			'', #Clave int. Tel
			s.lada_phone_number,#Lada Tel
			s.phone_number,
			'',#Clave int. Cel
			'',#Lada Cel
			s.cellphone_number,
			s.email,
			'',#Insititucion Educativa 1
			'',#Insititucion Educativa 2
			'',#Insititucion Educativa 3
			'',#Comentario +
			'',#Clave origen 2
			s.prev_school,#Clave Escuela Procedencia +
			s.average,
			'',#Fecha Esperada Graduacion 
			'PIS' if s.first_time else 'PIN',#Ingreso, Primer_Ingreso_Nivel
			'',#Padre Titulo Trato
			'',#Padre Fallecido
			s.father_name,#Padre Nombre
			'',#Padre Ap.Paterno
			'',#Padre Ap.Materno
			'',#Padre Correo
			'',#Padre Clave int. 
			'',#Padre Lada 
			'',#Padre Tel .
			'',#Padre Ext. 
			'',#Madre Titulo Trato
			'',#Madre Fallecido
			s.mother_name,#Madre Nombre
			'',#Madre Ap. Paterno
			'',#Madre Ap. Materno
			'',#Madre Correo
			'',#Madre Clave int. 
			'',#Madre Lada 
			'',#Madre Tel .
			'',#Madre Ext. 
			'',#Tutor Titulo Trato
			'',#Tutor Fallecido
			'',#Tutor Nombre
			'',#Tutor Ap. Paterno
			'',#Tutor Ap. Materno
			'',#Tutor Correo
			'',#Tutor Clave int.
			'',#Tutor Lada 	
			'',#Tutor Tel .					
			'',#Tutor Ext.
			'',#Clave Semaforo
			'',#Titulado
			'',#Cedula Profesional
			'',#Clave int. Oficina
			'',#Lada oficina
			'',#Tel . Oficina
			'',#Ext. Oficina
			'',#Radio
			'',#Clave Radio
			'',#Correo laboral
			'',#Empresa	
			'',#Giro
			'',#Puesto
			'',#Area
			'',)#Hora de Contacto
		return '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s'%(params[0],params[1],params[2],params[3],params[4],params[5],params[6],params[7],params[8],params[9],params[10],params[11],params[12],params[13],params[14],params[15],params[16],params[17],params[18],params[19],params[20],params[21],params[22],params[23],params[24],params[25],params[26],params[27],params[28],params[29],params[30],params[31],params[32],params[33],params[34],params[35],params[36],params[37],params[38],params[39],params[40],params[41],params[42],params[43],params[44],params[45],params[46],params[47],params[48],params[49],params[50],params[51],params[52],params[53],params[54],params[55],params[56],params[57],params[58],params[59],params[60],params[61],params[62],params[63],params[64],params[65],params[66],params[67],params[68],params[69],params[70],params[71],params[72],params[73],params[74],params[75],params[76],params[77],params[78],params[79],params[80],params[81],params[82],params[83])

	def __unicode__(self):
		return self.name

