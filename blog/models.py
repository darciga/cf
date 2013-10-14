from django.db import models
from django.contrib.auth.models import User
import MySQLdb

# Create your models here.

class Comentario(models.Model):
	"""Comentario"""
	contenido = models.TextField(help_text='Escribe un comentario')
	fecha_coment = models.DateField(auto_now=True)

	def __unicode__(self):
		return self.contenido
class Estado(models.Model):
	"""Estado"""
	nom_estado = models.CharField(max_length=50)

	def __unicode__(self):
		return nom_estado

class Categoria(models.Model):
	"""Categoria"""
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField(help_text='Escribe una descripcion de la categoria')

class Entrada(models.Model):
	"""Entrada"""
	autor = models.ForeignKey(User)
	comentario = models.ForeignKey(Comentario)
	estado =  models.ForeignKey(Estado)
	titulo = models.CharField(max_length=100)
	contenido = models.TextField(help_text='Redacta el contenido')
	fecha_pub = models.DateField(auto_now=True)

	def __unicode__(self):
		return self.titulo

class Agregador(models.Model):
	"""agreador"""
	entrada = models.ForeignKey(Entrada)
	categoria = models.ManyToManyField(Categoria)