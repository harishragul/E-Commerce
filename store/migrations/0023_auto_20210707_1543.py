# Generated by Django 3.2.4 on 2021-07-07 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_alter_require_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='screen',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='screen',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
