# Generated by Django 3.2.4 on 2021-07-17 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_rename_discripton_require_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='approved',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='approved',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
