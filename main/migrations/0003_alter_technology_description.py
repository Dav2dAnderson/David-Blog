# Generated by Django 5.1.4 on 2024-12-05 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_technology'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]