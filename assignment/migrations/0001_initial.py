# Generated by Django 4.1.2 on 2022-11-13 14:24

import assignment.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('assignmentID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('assignmenttoken', models.UUIDField(default=uuid.UUID('9c26eb1b-f45e-4fca-81b3-071c332b793b'))),
                ('assignmentName', models.CharField(blank=True, max_length=200)),
                ('assignmentDesc', models.CharField(blank=True, max_length=200)),
                ('assignmentFile', models.FileField(upload_to=assignment.models.user_directory_path)),
                ('upload_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('groupID', models.UUIDField(blank=True)),
                ('submissionTime', models.DateTimeField(blank=True)),
                ('assignmentuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
