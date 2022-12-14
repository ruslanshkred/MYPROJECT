# Generated by Django 4.1.2 on 2022-12-09 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_comment', to='orders.order', verbose_name='Order to comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_comment', to=settings.AUTH_USER_MODEL, verbose_name='Comment')),
            ],
        ),
    ]
