# Generated by Django 3.2.7 on 2021-10-04 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="goods",
            name="slug",
            field=models.SlugField(blank=True, default=0, unique=True),
            preserve_default=False,
        ),
    ]