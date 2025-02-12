# Generated by Django 4.2.11 on 2024-03-24 20:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("watchlist", "0003_watchlist_platform"),
    ]

    operations = [
        migrations.AlterField(
            model_name="watchlist",
            name="platform",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="watchlist",
                to="watchlist.streamplatform",
            ),
        ),
        migrations.CreateModel(
            name="Review",
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
                (
                    "rating",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ]
                    ),
                ),
                ("description", models.CharField(max_length=200, null=True)),
                ("active", models.BooleanField(default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "watchlist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="watchlist.watchlist",
                    ),
                ),
            ],
        ),
    ]
