# Generated by Django 4.1.7 on 2023-04-04 20:34

from django.db import migrations

def populate_status(apps, schemaeditor):
    status = {
        "published": "A blog post that is visible to everyone.",
        "unpublished": "A blog post in draft mode, visible only to the author."
    }
    Status = apps.get_model("posts", "Status")
    for key, desc in status.items():
        status_ogj = Status(name=key, description=desc)
        status_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_status)
    ]
