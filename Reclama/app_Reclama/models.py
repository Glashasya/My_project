from django.db import models

# Create your models here.
'''
название
описание
торг
время создания
цена
время обновления


'''

class Advertisement(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)
    descr = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если уместен торг!')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'reclama'