# Generated by Django 5.0.7 on 2024-11-05 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choco_app', '0003_remove_flavor_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flavor',
            name='seasonal',
            field=models.CharField(choices=[('Spring', 'Spring'), ('Summer', 'Summer'), ('Autumn', 'Autumn'), ('Winter', 'Winter'), ('No season', 'No season')], max_length=20),
        ),
    ]
