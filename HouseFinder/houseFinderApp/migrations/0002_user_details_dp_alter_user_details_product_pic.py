# Generated by Django 5.0.6 on 2024-05-23 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houseFinderApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='dp',
            field=models.ImageField(blank=True, null=True, upload_to='dp_image'),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='product_pic',
            field=models.ImageField(blank=True, null=True, upload_to='product_image'),
        ),
    ]
