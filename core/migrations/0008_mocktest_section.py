# Generated by Django 5.1.6 on 2025-02-13 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_updation_delete_updations'),
    ]

    operations = [
        migrations.AddField(
            model_name='mocktest',
            name='section',
            field=models.CharField(choices=[('artificer apprentice', 'Artificer Apprentice'), ('navy tradesman', 'Navy Tradesman '), ('navy chargeman', 'Navy Chargeman '), ('indian navy entrance test', 'Indian Navy Entrance Test'), ('indian navy angniveer mr', 'Indian Navy Agniveer MR'), ('indian navy angniveer ssr', 'Indian Navy Agniveer SSR'), ('naval dockyard', 'Naval Dockyard')], max_length=30, null=True),
        ),
    ]
