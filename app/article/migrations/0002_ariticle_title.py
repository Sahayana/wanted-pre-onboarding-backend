# Generated by Django 3.2.13 on 2023-08-09 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ariticle",
            name="title",
            field=models.CharField(default="test", max_length=150),
            preserve_default=False,
        ),
    ]
