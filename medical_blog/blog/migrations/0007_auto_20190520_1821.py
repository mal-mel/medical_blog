# Generated by Django 2.2.1 on 2019-05-20 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190520_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
