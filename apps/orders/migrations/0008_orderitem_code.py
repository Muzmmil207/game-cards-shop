# Generated by Django 5.0 on 2024-04-25 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0007_alter_order_order_key"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="code",
            field=models.CharField(default="غير متوفر بعد", max_length=100),
        ),
    ]
