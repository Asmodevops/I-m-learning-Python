# Generated by Django 5.0.3 on 2024-04-21 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='update',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='feedback',
            name='update_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]