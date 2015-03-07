from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product, ProductCategory
from cart.views import get_order


class ShopMixin(object):
    """Adds categories and current order to render context"""
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        categories = ProductCategory.objects.all()
        data['categories'] = categories
        data['order'] = get_order(self.request)
        return data


class ProductList(ShopMixin, ListView):
    model = Product
    paginate_by = 16
    template_name = 'product_list.html'
    context_object_name = 'products'

    def __init__(self, *args, **kwargs):
        self.category = None
        super().__init__(*args, **kwargs)

    def get_category(self):
        category_id = self.kwargs.get('category_id')
        category = None
        if category_id:
            category = get_object_or_404(
                ProductCategory,
                id=category_id,
            )
            self.category = category
        return category

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.category:
            self.get_category()
        if self.category:
            queryset = queryset.filter(
                category=self.category,
            )
        return queryset

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['selected_category'] = self.get_category()
        return data


class ProductDetailed(ShopMixin, DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


class AboutUs(TemplateView):
    template_name = 'about_us.html'
