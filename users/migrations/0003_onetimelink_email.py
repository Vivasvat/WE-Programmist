# Generated by Django 4.2.13 on 2024-07-03 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_onetimelink'),
    ]

    operations = [
        migrations.AddField(
            model_name='onetimelink',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
