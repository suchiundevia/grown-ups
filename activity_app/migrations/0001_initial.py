# Generated by Django 3.1 on 2020-09-21 03:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_title', models.CharField(blank=True, max_length=150, null=True)),
                ('activity_description', models.TextField(blank=True, null=True)),
                ('activity_material', models.CharField(blank=True, max_length=250, null=True)),
                ('activity_date', models.DateTimeField(blank=True, null=True)),
                ('activity_start_time', models.DateTimeField(blank=True, null=True)),
                ('activity_end_time', models.DateTimeField(blank=True, null=True)),
                ('activity_post_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('activity_location', models.CharField(blank=True, max_length=150, null=True)),
                ('activity_suburb', models.CharField(blank=True, max_length=50, null=True)),
                ('attendance', models.IntegerField(blank=True, null=True)),
                ('activity_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Activities',
            },
        ),
    ]
