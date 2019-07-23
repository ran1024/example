from django import forms
from .models import Emaildata


class SendmailForm(forms.ModelForm):
    from_email = forms.EmailField(label='Эл.Почта')
    body = forms.CharField(label='Сообщение', widget=forms.Textarea)

    from_email.widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Ваш адрес эл.почты',
        'autofocus': True,
    })

    body.widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Введите сообщение',
    })

    class Meta:
        model = Emaildata
        fields = ('from_email', 'body',)
