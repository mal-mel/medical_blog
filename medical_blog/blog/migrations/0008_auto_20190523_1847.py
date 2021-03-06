# Generated by Django 2.2.1 on 2019-05-23 15:47

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190520_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='%Y/%m/%d/'),
        ),
    ]
