# Generated by Django 3.1.7 on 2021-06-22 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210622_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content_1',
            field=models.TextField(verbose_name='コンテンツ1*'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='作成日'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200, verbose_name='タイトル*'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日'),
        ),
    ]