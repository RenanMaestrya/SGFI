# Generated by Django 4.2.6 on 2023-12-02 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_print_withdrawn_at_alter_print_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='print',
            name='attachment',
            field=models.FileField(max_length=254, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='print',
            name='status',
            field=models.CharField(choices=[('pending', 'Pendente'), ('printed', 'Impresso'), ('withdrawn', 'Retirado')], default='pending', max_length=255),
        ),
    ]