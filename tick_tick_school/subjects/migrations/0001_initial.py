# Generated by Django 4.0.2 on 2022-03-18 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('teacher', models.CharField(max_length=200)),
                ('classroom', models.CharField(max_length=50)),
            ],
        ),
    ]
