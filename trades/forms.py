from django import forms
from products.models import Product
from models import Trades

class tradeForForm(forms.Form):
    class Meta:
        model = Trades
        fields = ('sender','offered', 'reciever','wanted')
