# Generated by Django 5.1.2 on 2024-10-28 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_leads', models.CharField(max_length=50)),
                ('whats_app_leads', models.CharField(max_length=12)),
                ('data_recebimento', models.CharField(max_length=8)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
