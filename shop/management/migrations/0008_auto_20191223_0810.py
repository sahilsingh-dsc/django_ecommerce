# Generated by Django 2.2.5 on 2019-12-23 08:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_auto_20191223_0647'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(default='', on_delete='', related_name='product', to='management.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
