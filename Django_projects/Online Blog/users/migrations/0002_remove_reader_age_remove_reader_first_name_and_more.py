# Generated by Django 4.0.4 on 2022-06-06 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reader',
            name='age',
        ),
        migrations.RemoveField(
            model_name='reader',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='reader',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='writer',
            name='age',
        ),
        migrations.RemoveField(
            model_name='writer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='writer',
            name='last_name',
        ),
        migrations.AddField(
            model_name='reader',
            name='username',
            field=models.CharField(blank=True, max_length=50, verbose_name='username'),
        ),
        migrations.AddField(
            model_name='writer',
            name='username',
            field=models.CharField(blank=True, max_length=50, verbose_name='username'),
        ),
    ]
