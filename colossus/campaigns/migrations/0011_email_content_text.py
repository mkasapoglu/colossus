# Generated by Django 2.0.6 on 2018-06-07 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0010_email_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='content_text',
            field=models.TextField(default='', verbose_name='content'),
            preserve_default=False,
        ),
    ]
