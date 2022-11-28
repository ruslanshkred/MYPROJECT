# Generated by Django 4.1.2 on 2022-11-22 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_book_book_genrie_book_book_genrie'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantity')),
                ('prise', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.book', verbose_name='Book in a cart')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='orders.cart', verbose_name='Cart')),
            ],
        ),
    ]
