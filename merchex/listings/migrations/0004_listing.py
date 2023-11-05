# Generated by Django 4.2.6 on 2023-10-13 21:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0003_alter_band_genre"),
    ]

    operations = [
        migrations.CreateModel(
            name="Listing",
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
                    "type",
                    models.CharField(
                        choices=[
                            ("Records", "Disques"),
                            ("Clothing", "Vetements"),
                            ("Posters", "Affiches"),
                            ("Miscellaneous", "Divers"),
                        ],
                        max_length=13,
                    ),
                ),
                ("description", models.CharField(max_length=1000)),
                ("sold", models.BooleanField(default=True)),
                ("year", models.IntegerField(default="")),
            ],
        ),
    ]