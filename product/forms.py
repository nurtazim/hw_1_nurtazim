from django import forms
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