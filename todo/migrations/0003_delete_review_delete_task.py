# Generated by Django 5.0.4 on 2024-04-13 12:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0002_review"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Review",
        ),
        migrations.DeleteModel(
            name="Task",
        ),
    ]
