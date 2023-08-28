# Generated by Django 4.2.4 on 2023-08-28 06:02

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='job_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='job_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('expiry_on', models.DateField()),
                ('job_description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('how_to_apply', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='jobs')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.job_category')),
            ],
        ),
    ]
