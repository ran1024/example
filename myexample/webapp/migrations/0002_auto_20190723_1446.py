# Generated by Django 2.2.3 on 2019-07-23 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emaildata',
            options={'verbose_name': 'Сообщение администратору', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.RemoveField(
            model_name='emaildata',
            name='subject',
        ),
    ]
