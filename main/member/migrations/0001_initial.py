# Generated by Django 4.2.5 on 2023-09-30 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('roll', models.IntegerField(blank=True, null=True)),
                ('deprt', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': ('Student',),
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('department', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=120, null=True)),
            ],
            options={
                'verbose_name_plural': ('Teacher',),
            },
        ),
    ]
