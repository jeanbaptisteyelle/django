# Generated by Django 2.2.10 on 2020-03-16 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('nom', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=255)),
                ('sujet', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_apdate', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': ' ',
                'verbose_name_plural': ' ',
            },
        ),
        migrations.CreateModel(
            name='newletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_apdate', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': ' ',
                'verbose_name_plural': ' ',
            },
        ),
    ]
