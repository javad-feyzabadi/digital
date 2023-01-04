from django.db import models
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):

    parent = models.ForeignKey('self' ,verbose_name='parent', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(_('title') ,max_length = 50)
    description = models.TextField(_('description'), blank = True)
    avatar = models.ImageField(_('avatar'), blank=True,upload_to='categories')
    is_enable = models.BooleanField(_('is enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_created=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class Product(models.Model):

    title = models.CharField(_('title'),max_length = 50)
    description = models.TextField(_('description'),blank = True)
    avatar = models.ImageField(_('avatar'),blank=True,upload_to='products')
    is_enable = models.BooleanField(_('is enable'),default=True)
    created_time = models.DateTimeField(_('created time'),auto_created=True)
    updated_time = models.DateTimeField(_('updated time'),auto_now=True)
    categories = models.ManyToManyField('category',verbose_name=_('category'),blank=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'


class File(models.Model):

    product = models.ForeignKey('Product',verbose_name=_('product'),on_delete=models.CASCADE)
    title = models.CharField(_('title'),max_length = 50)
    file = models.FileField(_('file'),upload_to ='files/%Y/%m/%d/')
    is_enable = models.BooleanField(_('is enable'),default=True)
    created_time = models.DateTimeField(_('created time'),auto_created=True)
    updated_time = models.DateTimeField(_('updated time'),auto_now=True)


    class Meta:
        db_table = 'files'
        verbose_name = 'file'
        verbose_name_plural = 'files'