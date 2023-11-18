# Generated by Django 4.2.5 on 2023-11-18 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseDepartamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(default='', max_length=200)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='BaseTrabajador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('primer_apellido', models.CharField(max_length=50)),
                ('segundo_apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateTimeField(default='', null=True)),
                ('edad', models.IntegerField()),
                ('annos_experiencia', models.IntegerField()),
                ('ocupacion', models.CharField(default='trabajador', max_length=50)),
                ('id_departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.basedepartamento')),
            ],
            options={
                'verbose_name': 'Trabajador',
                'verbose_name_plural': 'Trabajadores',
            },
        ),
    ]
