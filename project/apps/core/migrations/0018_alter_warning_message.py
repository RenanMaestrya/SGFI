# Generated by Django 4.2.6 on 2023-12-19 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_rename_social_name_user_usual_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warning',
            name='message',
            field=models.TextField(),
        ),
    ]