from django import forms
from hayotildizi.models import GuestModel
from django.utils.translation import gettext_lazy as _


class GuestForm(forms.ModelForm):
    fullname = forms.CharField(
        max_length=300,
        label=False,
        widget=forms.TextInput(
            {
                'class': 'form-control',
                'id': 'colFormLabel',
                'placeholder': _('Введите ваше имя'),
            }
        ),
        required=True
    )
    phone = forms.CharField(
        max_length=16,
        label=False,
        widget=forms.TextInput(
            {
                'class': 'form-control',
                'id': 'colFormLabel2',
                'placeholder': _('Введите ваш номер'),
            }
        ),
        required=True
    )

    class Meta:
        model = GuestModel
        fields = '__all__'
