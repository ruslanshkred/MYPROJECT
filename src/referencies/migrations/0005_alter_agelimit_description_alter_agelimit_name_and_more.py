# Generated by Django 4.1.2 on 2022-11-13 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referencies', '0004_agelimit_cover_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agelimit',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='agelimit',
            name='name',
            field=models.CharField(max_length=10, verbose_name='Age Limits'),
        ),
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=40, verbose_name="Author's Name"),
        ),
        migrations.AlterField(
            model_name='cover',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='cover',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Cover'),
        ),
        migrations.AlterField(
            model_name='genrie',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='genrie',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Genrie'),
        ),
        migrations.AlterField(
            model_name='publishinghouse',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='publishinghouse',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Publishing House'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='name',
            field=models.CharField(max_length=10, verbose_name='Rate'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Serie'),
        ),
        migrations.AlterField(
            model_name='units',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='units',
            name='name',
            field=models.CharField(max_length=10, verbose_name='Units'),
        ),
    ]
