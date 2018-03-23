# Generated by Django 2.0.3 on 2018-03-22 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180322_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='desc',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='文章描述'),
        ),
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.IntegerField(default=0, verbose_name='浏览数'),
        ),
    ]
