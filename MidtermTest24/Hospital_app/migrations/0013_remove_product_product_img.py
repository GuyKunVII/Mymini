# Generated by Django 4.2.7 on 2024-01-25 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital_app', '0012_rename_drug_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_img',
        ),
    ]
