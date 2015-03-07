from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import ProductDetailed, ProductList, AboutUs
from cart.views import OrderDetails


urlpatterns = patterns(
    '',
    url(r'^(?P<category_id>\d+)?$', ProductList.as_view(), name='products'),
    url(r'^product/(?P<pk>\d+)/$', ProductDetailed.as_view(), name='product'),
    url(r'^add/$', 'cart.views.add_to_cart', name='add_to_cart'),
    url(r'^cart/$', OrderDetails.as_view(), name='cart'),
    url(r'^finish/$', 'cart.views.close_order', name='finish'),
    url(r'^about/$', AboutUs.as_view(), name='about'),
    url(r'^admin/', include(admin.site.urls)),
) + static(
    settings.STATIC_URL
) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
