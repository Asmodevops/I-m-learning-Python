# Generated by Django 5.0.3 on 2024-04-21 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_cinema', '0002_feedback_film_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='update',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='feedback',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]