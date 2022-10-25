# Generated by Django 4.1.2 on 2022-10-25 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('role', models.IntegerField(choices=[(1, 'Student'), (2, 'Teacher')], default=1)),
                ('assignment_upload', models.BooleanField(choices=[(1, True), (2, False)], default=2)),
                ('answer_upload', models.BooleanField(choices=[(1, True), (2, False)], default=2)),
                ('firstname', models.CharField(blank=True, default=False, max_length=200)),
                ('lastname', models.CharField(blank=True, default=False, max_length=200)),
                ('stream', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
