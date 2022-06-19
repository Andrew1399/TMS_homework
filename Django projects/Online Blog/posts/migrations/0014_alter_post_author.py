# Generated by Django 4.0.4 on 2022-06-19 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_follow_unique_together'),
        ('posts', '0013_category_slug_alter_post_is_draft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.writer'),
        ),
    ]
