# Generated by Django 5.0.3 on 2024-04-21 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_feedback_update_feedback_update_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
