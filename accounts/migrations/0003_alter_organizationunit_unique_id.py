# Generated by Django 4.2 on 2023-05-02 10:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_organizationunit_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationunit',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('52e2a94c-84b9-4128-b4be-af33eb1aa0c5'), editable=False, unique=True),
        ),
    ]