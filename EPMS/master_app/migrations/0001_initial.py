# Generated by Django 4.1.7 on 2023-02-28 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_name', models.CharField(max_length=100)),
                ('o_email', models.EmailField(max_length=254)),
                ('o_password', models.CharField(max_length=32)),
                ('o_contact', models.CharField(max_length=100)),
                ('o_website', models.CharField(max_length=100)),
                ('o_address', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'organization',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_name', models.CharField(max_length=100)),
                ('e_email', models.EmailField(max_length=254)),
                ('e_password', models.CharField(max_length=32)),
                ('e_gender', models.CharField(max_length=25)),
                ('e_contact', models.CharField(max_length=100)),
                ('e_address', models.CharField(max_length=150)),
                ('o_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_app.organization')),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]