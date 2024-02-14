# Generated by Django 4.0 on 2022-03-20 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('tasks', '0001_initial'),
        ('subjects', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
        migrations.AddField(
            model_name='task',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.subject'),
        ),
    ]