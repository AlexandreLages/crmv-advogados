# Generated by Django 3.0.5 on 2020-05-30 02:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advogado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.CharField(default='', max_length=255, null=True)),
                ('celular', models.CharField(default='', max_length=255, null=True)),
                ('cpf', models.CharField(default='', max_length=255, null=True)),
                ('rg', models.CharField(default='', max_length=255, null=True)),
                ('oab', models.CharField(default='', max_length=255, null=True)),
                ('curriculo', models.TextField(default='', null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbAdvogado',
            },
        ),
    ]
