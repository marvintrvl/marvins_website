# Generated by Django 5.0.6 on 2024-05-19 08:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_remove_photo_description_remove_photo_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='photos.category'),
        ),
    ]
