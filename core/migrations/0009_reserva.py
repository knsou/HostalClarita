# Generated by Django 3.2 on 2021-05-28 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_proveedor_producto_id_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='reserva',
            fields=[
                ('id_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('rut_empresa', models.CharField(max_length=12)),
                ('rut_huesped', models.CharField(max_length=12)),
                ('id_tipo_habitacion', models.IntegerField()),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
            ],
            options={
                'db_table': 'reserva',
                'managed': True,
            },
        ),
    ]
