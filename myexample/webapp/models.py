from django.db import models


class Emaildata(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    sender = models.CharField(max_length=20, verbose_name='Имя пользователя')
    from_email = models.EmailField(verbose_name='email отправителя')
    body = models.TextField(max_length=256, verbose_name='Письмо')
    status = models.BooleanField(default=False, verbose_name='Статус')

    class Meta:
        verbose_name = 'Сообщение администратору'
        verbose_name_plural = 'Сообщения'
