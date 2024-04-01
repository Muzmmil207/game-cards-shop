from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label="Account email (can not be changed)",
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "email", "readonly": "readonly"}
        ),
    )
    first_name = forms.CharField(
        label="Firstname",
        min_length=4,
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "Username", "readonly": "readonly"}
        ),
    )
    last_name = forms.CharField(
        label="Username",
        min_length=4,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "last name",
            }
        ),
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Username"})
    )

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "username")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["email"].required = True
