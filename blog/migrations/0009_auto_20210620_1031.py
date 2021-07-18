# Generated by Django 3.1.7 on 2021-06-20 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blog_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='link',
            new_name='link_1',
        ),
        migrations.AddField(
            model_name='blog',
            name='link_2',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]