# Generated by Django 4.2.6 on 2023-10-13 21:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0004_listing"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="title",
            field=models.CharField(default="", max_length=20),
            preserve_default=False,
        ),
    ]
