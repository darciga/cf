from django.db import models

class categoria(models.Model):
	"""Control de categorias"""
	nombre 		= models.CharField(max_length = 50, verbose_name = 'Nombre')
	descripcion = models.TextField(verbose_name = 'Descripcion', blank = True, null = True)
	icono 		= models.ImageFile(upload_to = 'uploads/iconos/', blank = True, null = True)
	class Meta:
		verbose_name 		= u'Categorias'
		verbose_name_plural = u'Categorias' 
	def __unicode__(self):
		return self.nombre

class subCategoria(models.Model):
	"""Control de sub Categorias"""
	categoria 	= ForeignKey(categoria)
	nombre 		= models.CharField(max_length = 50, verbose_name = 'Nombre')
	descripcion = models.TextField(verbose_name = 'Descripcion', blank = True, null = True)
	slug 		= models.slugField(max_length = 100, default = '', blank = True, null = True)
	class Meta:
		verbose_name 		= u'Sub-categoria'
		verbose_name_plural = u'Sub-categoria'
	def __unicode__(self):
		return self.nombre

class estadosPais(models.Model):
	"""Control de estados del Pais"""
	nombre = models.CharField(max_length = 50, verbose_name = 'Nombre')
	class Meta:
		verbose_name 		= u'Estado del Pais'
		verbose_name_plural = u'Estados del Pais'
	def __unicode__(self):
		return nombre
		
class ciudad(models.Model):
	"""Control de ciudades"""
	estado 			= ForeignKey(estadosPais)
	nombre 		 	= models.CharField(max_length = 50, verbose_name = 'Nombre')
	imgDescritiva 	= models.ImageFile(upload_to = 'uploads/img/', blank = True, null = True, verbose_name = 'Emblema')
	slug   			= models.slugField(max_length = 100, default = '', blank = True, null = True)
	class Meta:
		verbose_name 		= u'Ciudad'
		verbose_name_plural = u'Ciudades'
	def __unicode__(self):
		return self.nombre
		