# Generated by Django 5.1 on 2024-09-05 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PingResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('is_active', models.BooleanField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
