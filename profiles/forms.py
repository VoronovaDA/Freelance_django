from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    """Форма для выбора роли пользователя"""

    ROLES = (
        ("customer", "Customer"),
        ("freelancer", "Freelancer"),
    )
    role = forms.ChoiceField(choices=ROLES)

    class Meta:
        model = User
        fields = ["username", "password", "email"]
