# Generated by Django 5.0 on 2024-04-22 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_alter_card_price_alter_game_created_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discount",
            name="discount_value",
            field=models.DecimalField(decimal_places=0, max_digits=7),
        ),
    ]
