# Generated by Django 4.2.6 on 2023-10-13 18:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="band",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="band",
            name="biography",
            field=models.CharField(default="", max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="band",
            name="genre",
            field=models.CharField(default="", max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="band",
            name="official_homepage",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="band",
            name="year_formed",
            field=models.IntegerField(
                default=1900,
                validators=[
                    django.core.validators.MinValueValidator(1900),
                    django.core.validators.MaxValueValidator(2023),
                ],
            ),
            preserve_default=False,
        ),
    ]
