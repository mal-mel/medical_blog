# Generated by Django 2.2.1 on 2019-05-02 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_news'),
    ]

    operations = [
        migrations.DeleteModel(
            name='News',
        ),
    ]
