# Generated by Django 2.0.6 on 2018-06-07 12:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0011_email_content_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
