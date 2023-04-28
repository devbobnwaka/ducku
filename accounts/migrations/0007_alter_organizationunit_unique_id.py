# Generated by Django 4.2 on 2023-04-28 17:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_organizationunit_unique_id_alter_section_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationunit',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('53e784ad-70e6-4813-ab15-a6d2da02159f'), editable=False, unique=True),
        ),
    ]
