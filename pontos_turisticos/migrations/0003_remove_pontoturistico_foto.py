# Generated by Django 4.1.4 on 2023-01-01 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pontos_turisticos", "0002_pontoturistico_foto"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pontoturistico",
            name="foto",
        ),
    ]
