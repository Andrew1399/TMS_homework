# Generated by Django 4.0.4 on 2022-06-09 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_reader_age_remove_reader_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writer',
            name='type_of_activity',
        ),
        migrations.AddField(
            model_name='writer',
            name='activity',
            field=models.CharField(blank=True, max_length=70, verbose_name='activity'),
        ),
    ]