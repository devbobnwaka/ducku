# Generated by Django 4.2 on 2023-04-28 17:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_section_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationunit',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('aaadcef7-ebfb-425d-a665-2d869640ad85'), editable=False, unique=True),
        ),
    ]