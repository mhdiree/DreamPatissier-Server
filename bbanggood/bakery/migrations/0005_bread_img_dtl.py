# Generated by Django 5.0.6 on 2024-08-05 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0004_alter_bread_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='bread',
            name='img_dtl',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
    ]