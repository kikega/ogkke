"""Formularios administracion"""

# Django
from django import forms


class ChangePasswordForm(forms.Form):
    """Formulario cambio de password"""

    password = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput()
    )

    def clean(self):
        """Verficamos si los dos password coinciden"""

        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('No coinciden los password')

        return data
