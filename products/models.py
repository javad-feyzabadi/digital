from django.db import models
from django.utils.translation import ugettext_lazy as _
class Category(models.models):
    parent = models.ForeignKey(self,verbose_name='parent',blank=True,null=True,on_delete=models.CASCADE)
    title = models.CharField(_('title'),max_length = 50)
    description = models.TextField(_('description'),blank = True)
    avatar = models.ImageField(_('avatar'),blank=True,upload_to='categories')
    is_enable = models.BooleanField(_('is enable'),default=True)
    created_time = models.DateTimeField(_('created time'),auto_created=True)
    updated_time = models.DateTimeField(_('updated time'),auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class Product(models.models):

    pass

class File(models.models):

    pass
