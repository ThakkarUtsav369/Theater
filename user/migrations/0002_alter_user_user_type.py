# Generated by Django 4.2.4 on 2023-08-15 07:43

# Django imports
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_type",
            field=models.CharField(
                choices=[
                    ("OWNER", "Owner"),
                    ("MANAGER", "Manager"),
                    ("USER", "User"),
                    ("UNKNOWN", "Unknown"),
                ],
                default="USER",
                max_length=10,
            ),
        ),
    ]