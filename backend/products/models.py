from django.db import models
from django.utils.translation import gettext_lazy as _



def product_image(instance, filename):
    return 'Product_image/{filename}'.format(filename=filename)

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(
        verbose_name=_("Product visibility"),
        help_text=_("Change product visibility"),
        default=True,
    )

    def __str__(self) -> str:
        return str(self.name)


class Product(models.Model):
    gender = [
        ('All', 'All'),
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    
    name = models.CharField(max_length=500)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    sex = models.CharField(choices=gender, default='All', max_length=50)
    SizeOrModels = models.CharField(max_length=50)
    description = models.TextField(verbose_name=_("description"), help_text=_("Not Required"), blank=True)
    regularPrice = models.DecimalField(
        verbose_name=_("Regular price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    discountPrice = models.DecimalField(
        verbose_name=_("Discount price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
        default=0
    )
    image1 = models.ImageField(_("Image field1"), upload_to=product_image)
    image2 = models.ImageField(_("Image field2"), upload_to=product_image)
    stock = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(
        verbose_name=_("Product visibility"),
        help_text=_("Change product visibility"),
        default=True,
    )

    def __str__(self) -> str:
        return str(self.name)

    def final_price(self):
        return self.regularPrice - self.discountPrice


