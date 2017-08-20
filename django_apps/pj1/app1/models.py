from django.db import models

# Create your models here.

class Shain(models.Model):

    status_list = (
        ('0', '退勤'),
        ('1', '出勤')
    )
    shain_id = models.CharField(verbose_name='id', primary_key=True, unique=True, max_length=10)
    name = models.CharField(verbose_name='name',  max_length=100)
    status = models.CharField(verbose_name='status', choices=status_list, blank = True, max_length=2)
    
    def  __str__(self):
        return self.name
    