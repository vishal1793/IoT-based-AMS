# Generated by Django 5.0.3 on 2024-04-18 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_asset_table_tpi_ins_asset_table_tpi_ren'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset_table',
            name='tpi_ins',
        ),
        migrations.RemoveField(
            model_name='asset_table',
            name='tpi_ren',
        ),
        migrations.AlterField(
            model_name='asset_table',
            name='asset_code',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='asset_table',
            name='asset_desc',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='asset_table',
            name='uid',
            field=models.CharField(max_length=256, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='kit_table',
            name='in_loc_place',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='kit_table',
            name='kit_id',
            field=models.CharField(max_length=256, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='kit_table2',
            name='kit_id',
            field=models.CharField(max_length=256, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='kit_table2',
            name='out_loc_place',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='locations',
            name='in_loc',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='locations',
            name='out_loc',
            field=models.CharField(max_length=256),
        ),
    ]
