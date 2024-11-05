# Generated by Django 5.0.7 on 2024-11-05 05:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choco_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flavor',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='customer_name',
            field=models.CharField(default='Anonymous', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inventory',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='allergies',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='flavor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='choco_app.flavor'),
        ),
    ]