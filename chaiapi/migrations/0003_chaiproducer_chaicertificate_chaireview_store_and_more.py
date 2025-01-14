# Generated by Django 5.1.4 on 2025-01-14 20:03

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chaiapi", "0002_chaivariety_description_chaivariety_name"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ChaiProducer",
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
                ("name", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="ChaiCertificate",
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
                ("certificate_name", models.CharField(max_length=100)),
                ("issued_date", models.DateField(default=django.utils.timezone.now)),
                ("valid_until", models.DateField(default=django.utils.timezone.now)),
                (
                    "chai",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="certificate",
                        to="chaiapi.chaivariety",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChaiReview",
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
                ("rating", models.IntegerField()),
                ("comment", models.TextField()),
                ("date_added", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "chai",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="chaiapi.chaivariety",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Store",
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
                ("name", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                (
                    "chai_varieties",
                    models.ManyToManyField(
                        related_name="stores", to="chaiapi.chaivariety"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                ("bio", models.TextField(blank=True, null=True)),
                (
                    "profile_picture",
                    models.ImageField(blank=True, null=True, upload_to="profile_pics/"),
                ),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
