# Generated by Django 4.2.6 on 2023-12-02 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_print_print_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='print',
            name='observation',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]