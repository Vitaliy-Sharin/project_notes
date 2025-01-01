from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=300, verbose_name='Название папки')
    date_create = models.DateTimeField(verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Папка'
        verbose_name_plural = 'Папки'
        ordering = ['user', 'name']

    def __str__(self):
        return f'{self.name}/{str(self.user)}'


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=300, verbose_name='Название заметки')
    note_text = models.TextField(max_length=50000, verbose_name='Текст заметки')
    date_create = models.DateTimeField(verbose_name='Дата создания')
    date_of_editing = models.DateTimeField(verbose_name='Дата последнего изменения')
    parent_folder = models.ForeignKey(Folder, on_delete=models.CASCADE, verbose_name='Родительская папка', default=None,
                                      null=True, blank=True)

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['user', 'name']

    def __str__(self):
        return f'{self.name}/{str(self.user)}'
