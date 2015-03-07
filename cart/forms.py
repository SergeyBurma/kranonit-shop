from django import forms
from cart.models import Order, OrderPosition
from catalog.models import Product


class AddToCartForm(forms.Form):
    product = forms.ModelChoiceField(Product.objects.all(), widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'address', 'phone']


class OrderPositionForm(forms.ModelForm):
    class Meta:
        model = OrderPosition
        fields = ['product', 'count']
        widgets = {
            'product': forms.HiddenInput
        }


OrderPositionFormset = forms.inlineformset_factory(
    Order,
    OrderPosition,
    OrderPositionForm,
    extra=0,
)
