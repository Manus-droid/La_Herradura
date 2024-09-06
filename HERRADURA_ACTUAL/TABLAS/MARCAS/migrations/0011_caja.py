# Generated by Django 5.1 on 2024-08-16 16:30

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MARCAS', '0010_remove_producto_categoria_remove_producto_edad_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('abierta', models.BooleanField(default=True, verbose_name='Caja Abierta')),
                ('fecha_hs_ap', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha y hora de apertura')),
                ('fecha_hs_cier', models.DateTimeField(default=django.utils.timezone.now, verbose_name='fecha y hora de cierre')),
                ('monto_ini', models.FloatField(verbose_name='Monto Inicial')),
                ('total_ing', models.FloatField(verbose_name='Total Ingresos')),
                ('total_egr', models.FloatField(verbose_name='Total Egresos')),
                ('empleado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MARCAS.empleado')),
                ('sucursal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MARCAS.sucursal')),
            ],
        ),
    ]
