# Generated by Django 2.2 on 2019-09-05 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='finish_at',
            field=models.DateTimeField(default='', verbose_name='Время завершения'),
        ),
    ]