# Generated by Django 3.2.4 on 2021-06-12 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='shop_id',
            new_name='shop_identity',
        ),
    ]
