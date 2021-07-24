from django import forms
from product.models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model=Products
        fields = "title price category  tags".split()
        widgets = {
            "title":forms.TextInput(
                attrs={
                    "class":"forms-control"
                }
            ),
            "price":forms.NumberInput(
                attrs={
                    "class":"forms-control"
                }
            ),
            "category":forms.Select(
                attrs={
                    "class": "forms-control"
                }
            ),
            "tags":forms.SelectMultiple(
                attrs={
                    "class": "forms-control"
                }
            )
        }
