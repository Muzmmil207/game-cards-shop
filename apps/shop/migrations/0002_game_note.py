# Generated by Django 5.0 on 2024-04-21 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="note",
            field=models.TextField(blank=True, null=True),
        ),
    ]
