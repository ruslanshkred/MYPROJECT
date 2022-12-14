# Generated by Django 4.1.2 on 2022-12-10 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_ordercomment_order_alter_ordercomment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercomment',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_comment', to='orders.order', verbose_name='Order to comment'),
        ),
    ]
