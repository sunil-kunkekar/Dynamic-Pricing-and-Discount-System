# Generated by Django 4.2.15 on 2024-08-13 02:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BulkProduct",
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
                ("name", models.CharField(max_length=255)),
                ("base_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("bulk_discount_threshold", models.IntegerField()),
                ("bulk_discount_percentage", models.FloatField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="FixedAmountDiscount",
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
                ("name", models.CharField(max_length=255)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PercentageDiscount",
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
                ("name", models.CharField(max_length=255)),
                ("percentage", models.FloatField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SeasonalProduct",
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
                ("name", models.CharField(max_length=255)),
                ("base_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("season_discount_percentage", models.FloatField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
