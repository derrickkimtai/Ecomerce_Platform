# Generated by Django 5.1.7 on 2025-03-20 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0009_delete_movie_product_image2_product_image3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image5',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image6',
        ),
    ]
