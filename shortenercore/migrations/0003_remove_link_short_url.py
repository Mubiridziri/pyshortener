# Generated by Django 4.0.6 on 2022-07-18 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortenercore', '0002_link_original_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='short_url',
        ),
    ]
