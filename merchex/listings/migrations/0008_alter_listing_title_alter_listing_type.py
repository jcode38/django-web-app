# Generated by Django 4.2.6 on 2023-10-13 21:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0007_listing_band"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="title",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="listing",
            name="type",
            field=models.CharField(
                choices=[
                    ("R", "Records"),
                    ("C", "Clothing"),
                    ("P", "Posters"),
                    ("M", "Misc"),
                ],
                max_length=13,
            ),
        ),
    ]
