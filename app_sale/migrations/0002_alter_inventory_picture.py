# Generated by Django 4.2.7 on 2023-12-02 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sale', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='inventory/%Y/%m/%d/'),
        ),
    ]
