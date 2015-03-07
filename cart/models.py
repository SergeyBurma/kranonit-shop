from django.db import models


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Opened at')
    closed_at = models.DateTimeField(verbose_name='Closed at', blank=True, null=True)
    is_closed = models.BooleanField(default=False, verbose_name='Is closed')
    is_processed = models.BooleanField(default=False, verbose_name='Is processed')
    phone = models.CharField(max_length=32, null=True)
    address = models.CharField(max_length=256, null=True)
    name = models.CharField(max_length=64, verbose_name='Contact name', null=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def price(self):
        total_price = 0
        for p in self.positions.all():
            total_price += p.price()
        return total_price


class OrderPosition(models.Model):
    order = models.ForeignKey('cart.Order', related_name='positions')
    product = models.ForeignKey('catalog.Product')
    count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Order position'
        verbose_name_plural = 'Order positions'
        ordering = ['-count']

    def price(self):
        return self.product.price * self.count
