# Generated by Django 5.1.7 on 2025-03-20 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0010_remove_product_image2_remove_product_image3_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image1',
            new_name='image',
        ),
    ]
