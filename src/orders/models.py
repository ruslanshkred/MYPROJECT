from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='carts',
        verbose_name="User Cart",
        null=True,
        blank=True
    )

    def total_costs(self):
        all_book_positions = self.books.all()
        total_costs = 0
        for book_positions in all_book_positions:
            total_costs += book_positions.price_per_position
        return total_costs

class BookInCart(models.Model):
    book = models.ForeignKey(
        'books.Book',
        verbose_name = 'Book in a cart',
        on_delete = models.PROTECT
    )
    cart = models.ForeignKey(
        'orders.Cart',
        verbose_name = 'Cart',
        related_name = 'books',
        on_delete = models.CASCADE
    )
    quantity = models.IntegerField(
        verbose_name = 'Quantity',
        default = 1
    )
    price = models.ForeignKey(
        'books.Book',
        verbose_name = 'Price per unit',
        related_name = 'book_price',
        on_delete = models.PROTECT
    )
    created_date = models.DateTimeField(
        verbose_name = 'Created date',
        auto_now = False,
        auto_now_add = True
    )
    updated_date = models.DateTimeField(
        verbose_name = 'Updated date',
        auto_now = True,
        auto_now_add = False
    )

    @property
    def price_per_position(self):
        return self.price.price * self.quantity

class Order(models.Model):
    status = models.ForeignKey(
        'referencies.Status',
        verbose_name='Status',
        related_name='order_status',
        on_delete=models.PROTECT,
        default=1
    )
    cart = models.OneToOneField(
        'orders.Cart',
        verbose_name = 'Cart',
        related_name = 'order',
        on_delete = models.PROTECT
    )
    phone = models.PositiveIntegerField(
        verbose_name='Phone number'
    )
    address = models.TextField(
        verbose_name='Delivery Address',
    )
    additional_info = models.TextField(
        verbose_name='Additional Information',
        null=True,
        blank=True
    ) 
    created_date = models.DateTimeField(
        verbose_name = 'Created date',
        auto_now = False,
        auto_now_add = True
    )
    updated_date = models.DateTimeField(
        verbose_name = 'Updated date',
        auto_now = True,
        auto_now_add = False
    )


class OrderComment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='order_comment',
        verbose_name="User"
    )
    order = models.ForeignKey(
        'orders.Order',
        verbose_name = 'Order to comment',
        related_name='order_comment',
        on_delete = models.CASCADE
    )
    comment = models.TextField(
        verbose_name= 'Comment'
    )
    created_date = models.DateTimeField(
        verbose_name = 'Created date',
        auto_now = False,
        auto_now_add = True
    )
    def __str__(self):
        return self.comment