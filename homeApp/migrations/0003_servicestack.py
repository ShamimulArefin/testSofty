# Generated by Django 4.1.1 on 2022-09-08 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0002_delete_servicestack'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceStack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_stacks', models.CharField(max_length=500)),
                ('service_stacks_icons', models.CharField(max_length=500)),
            ],
        ),
    ]
