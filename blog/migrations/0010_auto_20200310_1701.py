# Generated by Django 2.2.10 on 2020-03-10 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blogpageauthor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Post date'),
        ),
    ]
