# Generated by Django 5.1.4 on 2024-12-07 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_technology_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teammate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=150)),
                ('job', models.CharField(max_length=150)),
                ('introduction', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
