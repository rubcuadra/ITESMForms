# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import students.models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20150912_2358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno_preparatoria',
            name='district_and_zipcode',
        ),
        migrations.AddField(
            model_name='alumno_preparatoria',
            name='date_of_registration',
            field=models.DateField(default=datetime.datetime(2015, 11, 2, 0, 4, 34, 101873, tzinfo=utc), verbose_name='Fecha De Registro', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumno_preparatoria',
            name='district',
            field=models.CharField(max_length=200, verbose_name='Colonia', blank=True),
        ),
        migrations.AddField(
            model_name='alumno_preparatoria',
            name='gender',
            field=models.CharField(default='M', max_length=1, verbose_name='Sexo: ', choices=[(b'M', b'Masculino'), (b'F', b'Femenino')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumno_preparatoria',
            name='lada_phone_number',
            field=models.CharField(default=55, help_text=b'DF = 55', max_length=3, verbose_name='Lada de Telefono de Casa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumno_preparatoria',
            name='maternal_last_name',
            field=models.CharField(max_length=120, verbose_name='Apellido Materno', blank=True),
        ),
        migrations.AddField(
            model_name='alumno_preparatoria',
            name='paternal_last_name',
            field=models.CharField(default='LastNameP', max_length=120, verbose_name='Apellido Paterno'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumno_preparatoria',
            name='period',
            field=models.CharField(default='201511', max_length=6, verbose_name='Periodo: ', choices=[(b'201611', b'Semestral Enero-Mayo 2016'), (b'201612', b'Verano 2016'), (b'201613', b'Semestral Agosto -Diciembre 2016'), (b'201711', b'Semestral Enero-Mayo 2017'), (b'201712', b'Verano 2017'), (b'201713', b'Semestral Agosto -Diciembre 2017'), (b'201811', b'Semestral Enero-Mayo 2018'), (b'201812', b'Verano 2018'), (b'201813', b'Semestral Agosto -Diciembre 2017')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumno_preparatoria',
            name='zipcode',
            field=models.CharField(max_length=10, verbose_name='C.P.', blank=True),
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='cellphone_number',
            field=models.CharField(max_length=10, verbose_name='Celular', blank=True),
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='city_and_county',
            field=models.CharField(max_length=200, verbose_name='Ciudad y Estado', blank=True),
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='father_name',
            field=models.CharField(max_length=120, verbose_name='Nombre de Padre', blank=True),
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='graduation_date',
            field=models.DateField(verbose_name='Fecha de Graduacion ', blank=True),
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='high_school',
            field=models.CharField(max_length=120, verbose_name='Nombre de Secundaria', choices=[(b'D00093', b'Colegio La Salle'), (b'D00186', b'Instituto Rougier'), (b'D00199', b'Colegio Universitario de M\xc3\xa9xico'), (b'D00214', b'Instituto Cumbres A.C.'), (b'D00252', b'Instituto Nacional para la Educaci\xc3\xb3n de los Adultos'), (b'D00274', b'Colegio Brit\xc3\xa1nico'), (b'D00280', b'Colegio Oxford'), (b'D00326', b'Escuela Mexicana Americana (U.N.A.M.)'), (b'D00366', b'Col del Tepeyac'), (b'D00390', b'Cedros'), (b'D00406', b'Colegio Cristobal Col\xc3\xb3n A.C.'), (b'D00429', b'Instituto Tapachula A.C.'), (b'D00435', b'Centro Educativo Tom\xc3\xa1s Moro (U.N.A.M.)'), (b'D00438', b'Colegio Williams (U.N.A.M.)'), (b'D00449', b'Colegio Madrid (U.N.A.M.)'), (b'D00480', b'Colegio La Salle A.C.'), (b'D00503', b'Bachillerato Alexander Bain S.C. (U.N.A.M.)'), (b'D00527', b'Ovalle Monday'), (b'D00531', b'Instituto Cumbres'), (b'D00539', b'Anne Sullivan'), (b'D00660', b'Instituto Educativo Olinca (U.N.A.M.)'), (b'D00684', b'Academia Maddox'), (b'D00694', b'Nuevo Continente'), (b'D00714', b'Instituto Francisco Possenti'), (b'D00729', b'Colegio Sim\xc3\xb3n Bolivar'), (b'D00732', b'Instituto Juventud del Estado de M\xc3\xa9xico A.C. (U.N.A.M.)'), (b'D00850', b'Baden Powell'), (b'D00876', b'Instituto Mexicano Regina'), (b'D00929', b'Secundaria Federal Anexa a la Normal Superior'), (b'D00993', b'Colegio Franc\xc3\xa9s del Pedregal (U.N.A.M.)'), (b'D00998', b'Instituto Rosedal'), (b'D01038', b'Colegio Green Hills S.C.'), (b'D01139', b'Liceo Franco-Mexicano A.C.'), (b'D01148', b'Leopoldo Ayala'), (b'D01279', b'The American School Foundation A.C. (U.N.A.M)'), (b'D01451', b'Fernando R. Rodr\xc3\xadguez'), (b'D01476', b'Instituto Rudyard Kipling'), (b'D01507', b'Instituto Miguel Angel A.C. (U.N.A.M.)'), (b'D01515', b'Reina Mar\xc3\xada'), (b'D01574', b'Colegio Vista Hermosa (U.N.A.M.)'), (b'D01583', b'Instituto T\xc3\xa9cnico y Cultural (U.N.A.M.)'), (b'D01698', b'Colegio Columbia College Panamericano'), (b'D01756', b'EMI Chapel School'), (b'D01757', b'Liceo Mexicano Japon\xc3\xa9s A.C. (U.N.A.M.)'), (b'D01771', b'Instituto Salamanca'), (b'D01810', b'Escuela Moderna Americana (U.N.A.M.)'), (b'D01814', b'Secundaria Benjam\xc3\xadn Franklin'), (b'D01844', b'Colegio Brit\xc3\xa1nico The Edron Academy'), (b'D01865', b'Escuela Reyna Isabel'), (b'D02166', b'Ignacio M. Altamirano'), (b'D02168', b'Instituto Irland\xc3\xa9s'), (b'D02173', b'Escuela Secundaria y Preparatoria de la Ciudad de M\xc3\xa9xico (U.N.A.M.)'), (b'D02232', b'Centro Cultural de la Ciudad de M\xc3\xa9xico'), (b'D02271', b'Colegio Franco Ingl\xc3\xa9s (U.N.A.M.)'), (b'D02312', b'Centro de Integraci\xc3\xb3n Educativa'), (b'D02329', b'Colegio Franc\xc3\xa9s Pasteur'), (b'D02546', b'Colegio del Bosque'), (b'D02555', b'Ridge Field High School'), (b'D02607', b'Colegio Israelita de M\xc3\xa9xico A.C. (U.N.A.M.)'), (b'D02612', b'Rafael Minor Franco'), (b'D02672', b'Escuela Ameyalli'), (b'D03118', b'Colegio Avante'), (b'D03124', b'Colegio Miraflores (U.N.A.M.)'), (b'D03319', b'Part. No. 0106 Centro Escolar Cedros'), (b'D03468', b'Instituto Cultural Franc\xc3\xa9s'), (b'D03737', b'Colegio Hebreo Maguen David'), (b'D03760', b'Cedros'), (b'D03863', b'Colegio Peterson'), (b'D03864', b'Instituto Asunci\xc3\xb3n de M\xc3\xa9xico A.C. (U.N.A.M.)'), (b'D03947', b'Colegio Garside'), (b'D04076', b'Escuela Sierra Nevada'), (b'D04091', b'Manuel Acosta'), (b'D04188', b'Instituto Romera'), (b'D04218', b'Colegio Bilbao'), (b'D04461', b'Deepwater Junior High School'), (b'D05034', b'Greengates School'), (b'D05253', b'Centro de Estudios Lomas'), (b'D05691', b'Sara Alarc\xc3\xb3n'), (b'D05753', b'Colegio Walden Dos'), (b'D05796', b'Instituto Pedag\xc3\xb3gico Anglo Espa\xc3\xb1ol'), (b'D06472', b'Sim\xc3\xb3n Bolivar del Pedregal'), (b'D06565', b'Instituto Luis Vives'), (b'D06566', b'Colegio Rossland'), (b'D07766', b'Instituto Rafael Rossi'), (b'D08456', b'Colegio Brit\xc3\xa1nico'), (b'D08487', b'Colegio Irland\xc3\xa9s OFarril'), (b'D08521', b'Colegio Aberdeen'), (b'D08533', b'Part. No. 0191 Centro Escolar del Tepeyac S.C.'), (b'D08631', b'Instituto Asunci\xc3\xb3n de M\xc3\xa9xico'), (b'D08633', b'Centro Educativo Jean Piaget'), (b'D08648', b'Instituto San Angel del Sur S.C.'), (b'D08652', b'Tarbut'), (b'D08653', b'Colegio Merici'), (b'D08654', b'Colegio Vista Hermosa'), (b'D08659', b'Colegio de San Ignacio de Loyola (Vizcainas)'), (b'D08661', b'Instituto Juventud'), (b'D08669', b'Instituto Hispano Ingl\xc3\xa9s de M\xc3\xa9xico'), (b'D08749', b'Colegio Hebreo Monte Sina\xc3\xad'), (b'D08750', b'Colegio Peterson'), (b'D08753', b'Instituto Mar\xc3\xada Canales'), (b'D08806', b'Part No. 0303 Sierra Nevada S.C.'), (b'D08893', b'Part No. 0230 Helen Keller A.C.'), (b'D08900', b'Escuela Secundaria Columbia'), (b'D08905', b'Instituto M\xc3\xa9xico Secundaria A.C.'), (b'D09006', b'Colegio Sim\xc3\xb3n Bolivar'), (b'D09050', b'Ofic. No. 0191 Mois\xc3\xa9s S\xc3\xa1enz'), (b'D09194', b'Colegio Ingl\xc3\xa9s Michael Faraday'), (b'D09555', b'David Livingstone'), (b'D09558', b'Mar\xc3\xada Montessori'), (b'D09585', b'Instituto Don Bosco Huichapan Salesiano'), (b'D09733', b'Colegio Eton S.C.'), (b'D09762', b'Colegio Hebreo Sefaradi A.C.'), (b'D09790', b'Westhill Institute'), (b'D09792', b'Escuela Secundaria y Preparatoria Justo Sierra'), (b'D09833', b'Part. No. 0193 Colegio Panamericano Texcoco'), (b'D09875', b'Colegio San Patricio - Cumbres'), (b'D10168', b'Centro Escolar La Paz'), (b'D10332', b'Rafael Donde'), (b'D10341', b'Colegio Britania'), (b'D10343', b'Isabel Grasseteau'), (b'D10350', b'Alexander Dul'), (b'D10351', b'Instituto San Angel Inn'), (b'D10353', b'Colegio Belfort'), (b'D10356', b'Jos\xc3\xa9 Guadalupe Posada'), (b'D10459', b'Dolores Angela Castillo'), (b'D10460', b'Colegio Bosques del Contadero'), (b'D10463', b'Colegio Eton S.C.'), (b'D10466', b'Escuela Secundaria T\xc3\xa9cnica 48'), (b'D10468', b'Antonio Castro Leal'), (b'D10469', b'Campestre de M\xc3\xa9xico'), (b'D10470', b'Colegio Eugenio de Mazenod A.C.'), (b'D10490', b'Instituto de Ense\xc3\xb1anza Actualizada'), (b'D10494', b'Montessori'), (b'D10506', b'Colegio Williams'), (b'D10507', b'General Arnulfo R. G\xc3\xb3mez'), (b'D10508', b'Escuela Inglesa Kent'), (b'D10557', b'Colegio Lindavista A.C.'), (b'D10751', b'Domingo Savio'), (b'D10775', b'Luz Savi\xc3\xb1\xc3\xb3n'), (b'D10817', b'Colegio Galileo Galilei'), (b'D10882', b'Tom\xc3\xa1s Alva Edison'), (b'D11178', b'Instituto Andes de Tuxtla S.C.'), (b'D11350', b'Instituto Cumbres'), (b'D11435', b'Colegio Independencia'), (b'D12374', b'The American School Foundation A.C.'), (b'D12493', b'Sec. Tec. Comercial No. 0028 Guadalupe Victoria'), (b'D12516', b'Westhill Institute'), (b'D12607', b'Berta Von Glumer'), (b'D12872', b'Centro Educativo Anglo Mexicano'), (b'D12908', b'Instituto Cervantes'), (b'D13181', b'Montessori'), (b'D14018', b'Escuela Sierra Nevada S.C. Interlomas'), (b'D14836', b'Colegio Ciudad de M\xc3\xa9xico'), (b'D14842', b'Escuela Secundaria Ofic. No. 0530 Anexa a la Normal de Atizap\xc3\xa1n de Zar'), (b'D15354', b'Instituto Fray Juan de Zumarraga'), (b'D15581', b'Instituto Cumbres Mexico'), (b'D15858', b'The Churchill School'), (b'D16270', b'Academie Ste Cecile International School'), (b'D16701', b'Colegio del Valle '), (b'D16703', b'Colegio Alamo  '), (b'D17366', b'Colegio Columbia'), (b'D17519', b'Part No 0406 British American School S C'), (b'D18341', b'Colegio Queen Elizabeth S C'), (b'D18599', b'Colegio Grimm Campus Santa Fe'), (b'D18688', b'Instituto Cumbres'), (b'D18882', b'Instituto Nacional para la Educacion de los Adultos'), (b'D18927', b'Gymnasium Ehingen'), (b'D19107', b'Instituto Rosedal Secundaria Lomas'), (b'D19140', b'Instituto Highlands de Toluca'), (b'D19306', b'Sec. Oficial 0300 Felipe Santiago Xicotencatl'), (b'D19563', b'Centro de Educacion Secundaria Personalizada'), (b'D21016', b'Ecole Nouvelle de la Suisse Romande'), (b'D21969', b'COLEGIO ANGLO AMERICANO LOMAS'), (b'D22443', b'Colegio Giocosa'), (b'D27268', b'Floresta'), (b'D61142', b'Winpenny School'), (b'D61142', b'Winpenny School'), (b'D61776', b'COMUNIDAD EDUCATIVA TOMAS MORO DOS'), (b'D63709', b'Valparaiso Institute'), (b'D64336', b'Colegio Lomas Hill'), (b'D64663', b'WILLIAM JAMES JUNIOR HIGH SCHOOL'), (b'D93225', b'Escuela Leonesa'), (b'D93227', b'Colegio Tiyoli'), (b'D93227', b'Colegio Tiyoli'), (b'H00035', b'Instituto La Salle A.C.'), (b'H00093', b'Colegio La Salle'), (b'H00150', b'ITESM Campus Saltillo'), (b'H00158', b'ITESM Campus Quer\xc3\xa9taro'), (b'H00163', b'ITESM Campus Toluca'), (b'H00165', b'ITESM Campus Ciudad de M\xc3\xa9xico'), (b'H00166', b'ITESM Campus Laguna'), (b'H00167', b'ITESM Campus Hidalgo'), (b'H00168', b'ITESM Campus Estado de M\xc3\xa9xico'), (b'H00169', b'ITESM Campus Cuernavaca'), (b'H00171', b'ITESM Campus Central de Veracruz'), (b'H00280', b'Colegio Oxford'), (b'H00322', b'Centro Universitario M\xc3\xa9xico (U.N.A.M.)'), (b'H00331', b'Colegio Erasmo de Rotterdam'), (b'H00404', b'Colegio La Salle'), (b'H00435', b'Centro Educativo Tom\xc3\xa1s Moro (U.N.A.M.)'), (b'H00438', b'Colegio Williams (U.N.A.M.)'), (b'H00503', b'Bach Alexander Bain S.C.'), (b'H00517', b'Universidad La Salle'), (b'H00531', b'Inst Cumbres'), (b'H00618', b'Instituto de Humanidades y Ciencias (U.N.A.M.)'), (b'H00711', b'Colegio Indoamericano (U.N.A.M.)'), (b'H00714', b'Instituto Francisco Possenti'), (b'H00736', b'Instituto Cultural Sucre'), (b'H00836', b'Universidad del Valle de M\xc3\xa9xico - Roma'), (b'H00876', b'Instituto Mexicano Regina'), (b'H00886', b'Direcci\xc3\xb3n de Sistemas Abiertos SEP'), (b'H00895', b'Cen Universitario Dr. Emilio C\xc3\xa1rdenas S.C.'), (b'H00993', b'Colegio Franc\xc3\xa9s del Pedregal (U.N.A.M.)'), (b'H00998', b'Instituto Rosedal'), (b'H01139', b'Liceo Franco Mexicano'), (b'H01221', b'Colegio Americano de Tabasco'), (b'H01279', b'The American School Foundation A.C. (U.N.A.M)'), (b'H01319', b'Centro de Educaci\xc3\xb3n y Cultura Ajusco (C.E.Y.C.A.)'), (b'H01476', b'Prep Rudyard Kipling'), (b'H01507', b'Instituto Miguel Angel A.C. (U.N.A.M.)'), (b'H01515', b'Col Reina Mar\xc3\xada'), (b'H01551', b'Colegio Marymount'), (b'H01572', b'Colegio Hispano Americano (U.N.A.M.)'), (b'H01574', b'Colegio Vista Hermosa (U.N.A.M.)'), (b'H01585', b'Centro Escolar del Lago A.C. (U.N.A.M.)'), (b'H01689', b'Institut Mont-Olivet'), (b'H01698', b'Colegio Columbia A.C.'), (b'H01757', b'Liceo Mexicano Japon\xc3\xa9s A.C. (U.N.A.M.)'), (b'H01806', b'Colegio Hebreo Tarbut (U.N.A.M.)'), (b'H01844', b'Colegio Brit\xc3\xa1nico The Edron Academy'), (b'H01864', b'Escuela Tom\xc3\xa1s Alva Edison'), (b'H02138', b'Colegio Juventus de Puebla A.C.'), (b'H02168', b'Instituto Irland\xc3\xa9s'), (b'H02172', b'Universidad Panamericana'), (b'H02271', b'Colegio Franco Ingl\xc3\xa9s (U.N.A.M.)'), (b'H02329', b'Colegio Franc\xc3\xa9s Pasteur'), (b'H02546', b'Colegio del Bosque'), (b'H02607', b'Colegio Israelita de M\xc3\xa9xico A.C. (U.N.A.M.)'), (b'H02654', b'Universidad Iberoamericana - Plantel Santa F\xc3\xa9'), (b'H02664', b'Escuela Bancaria y Comercial'), (b'H02672', b'Escuela Ameyalli'), (b'H02759', b'Colegio Biling\xc3\xbce Las Hayas S.C.'), (b'H03124', b'Colegio Miraflores'), (b'H03177', b'Colegio de Bachilleres Plantel 5'), (b'H03588', b'Colegio Anglo Mexicano de Coyoacan A.C.'), (b'H03737', b'Colegio Hebreo Maguen David'), (b'H03863', b'Colegio Peterson'), (b'H03873', b'The Lawrenceville School'), (b'H04041', b'Instituto Cenca S.C.'), (b'H04188', b'Instituto Romera'), (b'H04218', b'Colegio Bilbao'), (b'H04905', b'Colegio Victoria Tepeyac'), (b'H05034', b'Colegio Greengates'), (b'H05097', b'Preparatoria Abierta SEP'), (b'H05796', b'Instituto Pedag\xc3\xb3gico Anglo Espa\xc3\xb1ol'), (b'H06287', b'Colegio La Salle de Veracruz A.C.'), (b'H06295', b'Colegio San Juan Evangelista'), (b'H06464', b'Notre Dame Academy'), (b'H06472', b'Simon Bolivar del Pedregal'), (b'H06566', b'Colegio Rossland (U.N.A.M.)'), (b'H07049', b'Colegio Israelita Yavne'), (b'H08631', b'Instituto Asunci\xc3\xb3n de M\xc3\xa9xico A.C.'), (b'H08632', b'Universidad Panamericana'), (b'H08652', b'Colegio Hebreo Tarbut'), (b'H08653', b'Colegio Merici'), (b'H08654', b'Colegio Vista Hermosa'), (b'H08659', b'Colegio de San Ignacio de Loyola (Vizcainas)'), (b'H08669', b'Instituto Hispano Ingl\xc3\xa9s de M\xc3\xa9xico'), (b'H08671', b'Preparatoria Salesiana A.C.'), (b'H08749', b'Colegio Hebreo Monte Sina\xc3\xad'), (b'H08806', b'Escuela Sierra Nevada'), (b'H09620', b'Instituto Cumbres'), (b'H09688', b'Universidad An\xc3\xa1huac'), (b'H09762', b'Colegio Hebreo Sefaradi A.C.'), (b'H09790', b'Westhill Institute'), (b'H09802', b'Universidad del Valle de M\xc3\xa9xico Campus Chapultepec'), (b'H10463', b'Colegio Eton'), (b'H10508', b'Esc Inglesa Kent'), (b'H10751', b'Instituto Domingo Savio'), (b'H11307', b'Liceo Franc\xc3\xa9s de Madrid'), (b'H13321', b'Inst Miguel Angel A.C.'), (b'H13424', b'Escuela Sierra Nevada'), (b'H13819', b'ITESM Campus Santa Fe'), (b'H13917', b'ITESM Campus Santa Catarina'), (b'H13989', b'ITESM Campus Cumbres'), (b'H14074', b'ITESM Campus Morelia'), (b'H14983', b'Universidad Aut\xc3\xb3noma del  Estado de M\xc3\xa9xico Plantel Nezahualcoyotl'), (b'H15136', b'Leysin American School'), (b'H15300', b'Instituto Cumbres'), (b'H15689', b'Escuela de Bachilleres Coatepec'), (b'H15791', b'Instituto Lasalle de Guanajuato'), (b'H16701', b'Preparatoria ISEC Colegio del Valle'), (b'H17246', b'Colegio Cristobal Colon  A C'), (b'H18071', b'Universidad Tecnologica de Mexico UNITEC'), (b'H18406', b'Colegio Britania'), (b'H18666', b'Universidad del Valle de Mexico Campus Toluca'), (b'H18874', b'Universidad Tec Milenio Campus Ferreria'), (b'H18956', b'Goethe Gymnasium Freiburg'), (b'H19555', b'Universidad Latinoamericana Campus Florida'), (b'H20758', b'Preparatoria London'), (b'H60222', b'BACHILLERATO CENTRO EDUCATIVO EMMANUEL MOUNIER'), (b'H60483', b'Instituto Aberdeen'), (b'H60578', b'COLEGIO ATID'), (b'H61141', b'COLEGIO GRIMM CAMPUS SANTA FE BACHILLERATO'), (b'H61775', b'Instituto Emuna'), (b'H61777', b'Colegio Anglo Americano Lomas'), (b'H63737', b'Colegio El Roble'), (b'0', b'Otro')]),
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='mother_name',
            field=models.CharField(max_length=120, verbose_name='Nombre de Madre', blank=True),
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Nombre(s)'),
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='nationality',
            field=models.CharField(max_length=120, verbose_name='Nacionalidad', blank=True),
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='phone_number',
            field=models.CharField(max_length=8, verbose_name='Telefono de Casa'),
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='street_and_number',
            field=models.CharField(max_length=200, verbose_name='Calle y Numero', blank=True),
        ),
        migrations.AlterField(
            model_name='alumno_profesional',
            name='interests',
            field=models.CharField(max_length=130, verbose_name='Carreras de Interes', validators=[students.models.validate_length]),
        ),
        migrations.AlterField(
            model_name='alumno_profesional',
            name='starting_year',
            field=models.IntegerField(default=2015, verbose_name='Year de Ingreso', validators=[students.models.validate_year]),
        ),
    ]
