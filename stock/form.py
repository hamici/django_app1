from django import forms
from .models import Product

class productAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','price','stock_qte']
        labels = {'name':'nom du Produit','category':'categorie','price':'prix','stock_qte':'quantitée'}