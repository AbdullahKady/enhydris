# Generated by Django 2.1.7 on 2019-04-01 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("enhydris", "0009_remove_alt_fields")]

    operations = [
        migrations.AlterModelOptions(
            name="gentityaltcode",
            options={
                "ordering": ("type__descr", "value"),
                "verbose_name": "Alternative code",
                "verbose_name_plural": "Alternative codes",
            },
        ),
        migrations.AlterModelOptions(
            name="gentityevent",
            options={
                "ordering": ["-date"],
                "verbose_name": "Log entry",
                "verbose_name_plural": "Log entries",
            },
        ),
        migrations.AlterModelOptions(
            name="gentityfile",
            options={
                "ordering": ("descr",),
                "verbose_name": "File",
                "verbose_name_plural": "Files",
            },
        ),
        migrations.AlterModelOptions(
            name="instrument",
            options={
                "ordering": ("name",),
                "verbose_name": "Instrument",
                "verbose_name_plural": "Instruments",
            },
        ),
    ]
