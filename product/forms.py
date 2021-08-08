import datetime
import secrets

from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from product.models import ConfeirmCode
from product.models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model=Products
        fields = "title price category  tags".split()
        widgets = {
            "title":forms.TextInput(
                attrs={
                    "class":"form-control"
                }
            ),
            "price":forms.NumberInput(
                attrs={
                    "class":"form-control"
                }
            ),
            "category":forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),
            "tags":forms.SelectMultiple(
                attrs={
                    "class": "form-control"
                }
            )
        }
class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,min_length=3,widget=forms.TextInput(
        attrs={
            "class":"form-control"
        }
    ))
    password=forms.CharField(max_length=100,min_length=3,widget=forms.PasswordInput(
        attrs={
            "class":"form-control"
        }
    ))




class RegisterForm(forms.Form):
    username=forms.EmailField(max_length=100,min_length=3,
                              label="Email",
                              widget=forms.EmailInput(
        attrs={
            "class":"form-control"
        }
    ))
    password=forms.CharField(max_length=100,min_length=3,widget=forms.PasswordInput(
        attrs={
            "class":"form-control"
        }
    ))
    password1 = forms.CharField(max_length=100, min_length=3, widget=forms.PasswordInput(
        attrs={
            "class": "form-control"
        }
    ))
    def clean_username(self):
       username= self.cleaned_data["username"]
       if User.objects.filter(username=username).count()>0:
            raise ValidationError("Пользователь уже существует")
       return username
    def clean_password1(self):
        password = self.cleaned_data["password"]
        password1 = self.cleaned_data["password1"]
        if password != password1:
            raise ValidationError("Пароли не совпадают")
        return password1


    def save(self):
        user=User.objects.create_user(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["username"],
            password=self.cleaned_data["password"],
            is_active=False
        )
        user.save()

        code = secrets.token_urlsafe(6)
        ConfeirmCode.objects.create(code=code,
                                    user=user,
                                    valid_until=datetime.datetime.now()+datetime.timedelta(minutes=20))

        send_mail(
            message=f"http://127.0.0.1:8000/activate/{code}/",
            subject="Activation code",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.cleaned_data["username"]]
        )
        return user

class CheckForm(forms.Form):

    username=forms.CharField(max_length=100,min_length=3,widget=forms.TextInput(
        attrs={
            "class":"form-control"
        }
    ))
    password=forms.CharField(max_length=100,min_length=3,widget=forms.PasswordInput(
        attrs={
            "class":"form-control"
        }
    ))