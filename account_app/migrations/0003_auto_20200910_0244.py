# Generated by Django 3.1 on 2020-09-10 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0002_auto_20200908_2214'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name_plural': 'User Profile'},
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_profile', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='account_app.userprofile')),
            ],
            options={
                'verbose_name_plural': 'Visitor',
            },
        ),
        migrations.CreateModel(
            name='Organiser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_profile', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='account_app.userprofile')),
            ],
            options={
                'verbose_name_plural': 'Organiser',
            },
        ),
    ]
