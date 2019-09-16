from django.db import models

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class Article(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='Описание')

    full_description=models.TextField(max_length=1000, null=True, blank=False, verbose_name='Подробное описание')

    status = models.CharField(max_length=20, verbose_name='Статус', default=STATUS_CHOICES[0][0],
                                choices=STATUS_CHOICES)

    finish_at = models.DateField(max_length=20, default='', null=True, blank=True, verbose_name='Время завершения')





    def __str__(self):
        return "{}. {}".format(self.pk, self.description)


