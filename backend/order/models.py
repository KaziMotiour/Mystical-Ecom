from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
User = get_user_model()

# Create your models here.
class Voucher(models.Model):
    name = models.CharField(max_length=50)
    amount = models.IntegerField(default=0)
    is_active = models.BooleanField(
        verbose_name=_("Product visibility"),
        help_text=_("Change product visibility"),
        default=False,
    )

    def __str__(self) -> str:
        return self.name


class AddToCart(models.Model):
    user = models.ForeignKey(User, related_name='addToCart', on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.product



class PlaceOrder(models.Model):
    payment_status=[
        ('incomplete', 'incomplete'),
        ('complete', 'complete')
    ]
    payment_method=[
        ('nope', 'nope'),
        ('paypal', 'paypal'),
        ('sslcommerce', 'sslcommerce')
    ]
    dalivary_status=[
        ('picked', 'picked'),
        ('on the way', 'on the way'),
        ('delivared', 'delivared')
    ]
    user = models.ForeignKey(User, related_name='placeOrderdUser', on_delete=models.CASCADE)
    address = models.ForeignKey("accounts.Address", related_name='userAddress', on_delete=models.CASCADE)
    totalAmount = models.IntegerField()
    discountAmount = models.IntegerField()
    delivaryCost = models.IntegerField()
    finalAmount = models.IntegerField()
    voucher = models.OneToOneField(Voucher, related_name='vouchers', on_delete=models.CASCADE)
    paymentStatus = models.CharField(choices=payment_status, default='incomplete', max_length=50)
    paymentMethod = models.CharField(choices=payment_method, default='nope', max_length=50)
    paymentID = models.CharField(max_length=100)
    delivaryStatus = models.CharField(choices=dalivary_status, default='picked', max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.user)

class OrderdItem(models.Model):
    placeOrder = models.ForeignKey(PlaceOrder, related_name="orderItem",  on_delete=models.CASCADE)
    prduct = models.ForeignKey("products.Product", related_name="productList", on_delete=models.CASCADE)

