from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    record_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=10.00)

    class Meta:
        ordering = ('-record_date',)

    def __str__(self):
        return f'{self.title}'

    def image_sequence(self):
        return range(self.images.count())


class ProductImage(models.Model):
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images')
    record_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_update = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ('-record_date',)

    def __str__(self):
        return f'{self.product.title} - {self.image.url}'
