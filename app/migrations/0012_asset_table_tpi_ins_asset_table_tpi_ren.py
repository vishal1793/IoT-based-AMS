# Generated by Django 5.0.3 on 2024-04-18 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_asset_table_tpi_ins_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset_table',
            name='TPI_ins',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='asset_table',
            name='TPI_ren',
            field=models.DateField(blank=True, null=True),
        ),
    ]
