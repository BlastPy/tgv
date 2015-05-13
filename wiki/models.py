# coding: utf-8
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class NamePart(models.Model):
    """
    Назва частини типу ТЗСП. Тут тільки ід і сама назва це як над пункт.
    """
    title = models.CharField(max_length=255,verbose_name="Заголовок частини.")

    def get_absolute_url(self):
        return "/url/%i/" % self.id

    def __unicode__(self):
        return '%s' % (self.title)


class Rozdil(models.Model):
    """ 
    Назва  розділу для частини , + Та головний він чи допоміжний.
    """
    title = models.CharField(max_length=255,verbose_name="Назва розділу")
    part_of = models.ForeignKey(NamePart,verbose_name="В частині")
    is_main = models.BooleanField(default=1,verbose_name="Головний ?")

    def get_absolute_url(self):
        return "/rozdil/%i/" % self.id

    def __unicode__(self):
        return '%s' % (self.title)

class Stats(models.Model):
    """
    Загальні характеристики, відноситься до розділу
    """
    name = models.CharField(max_length=170,verbose_name="Імя ?")
    image = models.ImageField(upload_to='media')
    robota =  RichTextField(verbose_name="Опис роботи")
    opus_ustanovku = RichTextField(verbose_name="Опис установки")
    zag_bund = RichTextField(verbose_name="Загальна будова")
    tth = RichTextField(verbose_name="ТТХ")
    teh_obslug = RichTextField(verbose_name="Технічне обслуговування")
    main_is = models.ForeignKey(Rozdil,verbose_name="З розділу")

    def get_absolute_url(self):
        return "/detali/%i/" % self.id

    def __unicode__(self):
        return '%s %s' % (self.name, self.main_is)


