# Generated by Django 4.1.2 on 2022-11-29 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_profile_first_name_profile_group_profile_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Phone number'),
        ),
    ]
