# Generated by Django 5.1.4 on 2024-12-23 11:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ChaiVariety",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data_added", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("ML", "MASALA"),
                            ("GI", "GINGER"),
                            ("KL", "KIWI"),
                            ("PL", "PLAIN"),
                            ("EL", "ELAICHI"),
                        ],
                        default="ML",
                        max_length=2,
                    ),
                ),
            ],
        ),
    ]
