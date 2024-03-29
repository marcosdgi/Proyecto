# Generated by Django 4.2.5 on 2023-11-19 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Informe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(unique=True)),
                ('modificaciones', models.CharField(default='', max_length=50)),
                ('id_contrato', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.contrato')),
            ],
            options={
                'verbose_name': 'Informe',
                'verbose_name_plural': 'Informes',
            },
        ),
    ]
