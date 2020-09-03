# Generated by Django 3.0.7 on 2020-09-03 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cases", "0003_auto_20200727_1348"),
    ]

    operations = [
        migrations.AddField(
            model_name="case",
            name="description",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="case",
            name="name",
            field=models.CharField(default="Case name", max_length=200),
            preserve_default=False,
        ),
    ]