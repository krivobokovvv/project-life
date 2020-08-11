from colorfield.fields import ColorField
from django.db import models
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail import ImageField


class Book(models.Model):
	name = models.CharField(verbose_name=_('Title'), max_length=200)
	author = models.CharField(verbose_name=_('Author'), max_length=200)
	tags = models.ManyToManyField('Tag', blank=True)
	preview = models.ForeignKey('Page', verbose_name=_('Preview'), on_delete=models.SET_NULL, blank=True, null=True)

	class Meta:
		verbose_name = _('Book')
		verbose_name_plural = _('Books')

	def __str__(self):
		return self.name


class Chapter(models.Model):
	book = models.ForeignKey('Book', verbose_name=_('Book'), on_delete=models.CASCADE)
	name = models.CharField(verbose_name=_('Title'), max_length=50)
	count_page = models.IntegerField(verbose_name=_('Count page'), default=0)

	class Meta:
		verbose_name = _('Chapter')
		verbose_name_plural = _('Chapters')

	def __str__(self):
		return self.name


class Page(models.Model):
	chapter = models.ForeignKey('Chapter', verbose_name=_('Chapter'), on_delete=models.CASCADE)
	number = models.IntegerField(verbose_name=_('Number'))
	image = ImageField(verbose_name=_('Image'), upload_to='image/%Y/%m/%d/')

	class Meta:
		verbose_name = _('Page')
		verbose_name_plural = _('Pages')

		unique_together = ('chapter', 'number')
		ordering = ['chapter', 'number']

	def __str__(self):
		page_test = _('Page')
		return f'{self.chapter.book} / {self.chapter} / {page_test} {self.number}'


class Tag(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=50)
	color = ColorField(verbose_name=_('Color'), default='#FFFFFF')

	class Meta:
		verbose_name = _('Tag')
		verbose_name_plural = _('Tags')

	def __str__(self):
		return self.name
