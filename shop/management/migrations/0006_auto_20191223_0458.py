# Generated by Django 2.2.5 on 2019-12-23 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_slider'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='slider1',
            new_name='slider_image',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='slider2',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='slider3',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='slider4',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='slider5',
        ),
    ]