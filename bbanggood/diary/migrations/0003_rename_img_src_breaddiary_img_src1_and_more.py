# Generated by Django 5.0.6 on 2024-08-01 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_breaddiary_img_src'),
    ]

    operations = [
        migrations.RenameField(
            model_name='breaddiary',
            old_name='img_src',
            new_name='img_src1',
        ),
        migrations.AddField(
            model_name='breaddiary',
            name='img_src2',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='breaddiary',
            name='img_src3',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
    ]