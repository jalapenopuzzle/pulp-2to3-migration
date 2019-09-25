# Generated by Django 2.2.5 on 2019-09-25 13:54

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0007_delete_progress_proxies'),
    ]

    operations = [
        migrations.CreateModel(
            name='MigrationPlan',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('plan', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pulp2Content',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('pulp2_id', models.CharField(max_length=255)),
                ('pulp2_content_type_id', models.CharField(max_length=255)),
                ('pulp2_last_updated', models.PositiveIntegerField()),
                ('pulp2_storage_path', models.TextField(null=True)),
                ('downloaded', models.BooleanField(default=False)),
                ('pulp3_content', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Content')),
            ],
            options={
                'unique_together': {('pulp2_id', 'pulp2_content_type_id')},
            },
        ),
        migrations.CreateModel(
            name='Pulp2Repository',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('pulp2_object_id', models.CharField(max_length=255, unique=True)),
                ('pulp2_repo_id', models.CharField(max_length=255)),
                ('pulp2_description', models.TextField(null=True)),
                ('pulp2_last_unit_added', models.DateTimeField(null=True)),
                ('pulp2_last_unit_removed', models.DateTimeField(null=True)),
                ('is_migrated', models.BooleanField(default=False)),
                ('pulp3_repository_version', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.RepositoryVersion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pulp2Importer',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('pulp2_object_id', models.CharField(max_length=255, unique=True)),
                ('pulp2_type_id', models.CharField(max_length=255)),
                ('pulp2_config', django.contrib.postgres.fields.jsonb.JSONField()),
                ('pulp2_last_updated', models.DateTimeField()),
                ('is_migrated', models.BooleanField(default=False)),
                ('pulp2_repository', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pulp_2to3_migration.Pulp2Repository')),
                ('pulp3_remote', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Remote')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pulp2RepoContent',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('pulp2_unit_id', models.CharField(max_length=255)),
                ('pulp2_content_type_id', models.CharField(max_length=255)),
                ('pulp2_repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pulp_2to3_migration.Pulp2Repository')),
            ],
            options={
                'unique_together': {('pulp2_repository', 'pulp2_unit_id')},
            },
        ),
        migrations.CreateModel(
            name='Pulp2ISO',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('checksum', models.CharField(max_length=64)),
                ('size', models.BigIntegerField()),
                ('pulp2content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iso_detail_model', to='pulp_2to3_migration.Pulp2Content')),
            ],
            options={
                'default_related_name': 'iso_detail_model',
                'unique_together': {('name', 'checksum', 'size', 'pulp2content')},
            },
        ),
        migrations.CreateModel(
            name='Pulp2Distributor',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('pulp2_object_id', models.CharField(max_length=255, unique=True)),
                ('pulp2_id', models.CharField(max_length=255)),
                ('pulp2_type_id', models.CharField(max_length=255)),
                ('pulp2_config', django.contrib.postgres.fields.jsonb.JSONField()),
                ('pulp2_auto_publish', models.BooleanField()),
                ('pulp2_last_updated', models.DateTimeField()),
                ('is_migrated', models.BooleanField(default=False)),
                ('pulp2_repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pulp_2to3_migration.Pulp2Repository')),
                ('pulp3_distribution', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.BaseDistribution')),
                ('pulp3_publication', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Publication')),
                ('pulp3_publisher', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Publisher')),
            ],
            options={
                'unique_together': {('pulp2_repository', 'pulp2_id')},
            },
        ),
    ]
