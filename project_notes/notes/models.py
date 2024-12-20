from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    name = models.CharField(max_length=300, verbose_name='Название заметки')
    note_text = models.TextField(max_length=20000, verbose_name='Текст заметки')
    date_create = models.DateTimeField(verbose_name='Дата создания')
    date_of_editing = models.DateTimeField(verbose='Дата последнего изменения')

    def __str__(self):
        return f'{self.name}/{self.user.name}'