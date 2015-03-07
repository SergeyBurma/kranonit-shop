import datetime
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from cart.models import Order, OrderPosition
from cart.forms import AddToCartForm, OrderForm, OrderPositionFormset


def get_order(request):
    order_id = request.session.get('order_id')
    order = None
    if order_id:
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            pass
    return order


def add_to_cart(request):
    order = get_order(request)
    if not order:
        order = Order.objects.create()
        request.session['order_id'] = order.id
    form = AddToCartForm(request.POST)
    if form.is_valid():
        product = form.cleaned_data['product']
        order_position, created = OrderPosition.objects.get_or_create(
            product=product,
            order=order,
        )
        order_position.count += 1
        order_position.save()
    print(form.errors)
    return redirect('cart')


def close_order(request):
    if request.POST:
        order = get_order(request)
        order.is_closed = True
        order.closed_at = datetime.datetime.now()
        order.save()
        return render(request, 'close_order.html', {
            'order': order,
        })
    else:
        return redirect('order')


class OrderDetails(UpdateView):
    model = Order
    template_name = 'cart.html'
    form_class = OrderForm
    success_url = '/finish'

    def get_object(self, queryset=None):
        return get_order(self.request)

    def get_formset(self):
        return OrderPositionFormset(**self.get_form_kwargs())

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['formset'] = self.get_formset()
        return data

    def form_valid(self, form):
        formset = self.get_formset()
        if formset.is_valid():
            for position_form in formset:
                position_form.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
