# Generated by Django 3.1.4 on 2020-12-08 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fameza', '0007_auto_20201208_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Pedido Confirmado', 'Pedido Confirmado'), ('Por Entregar', 'Por Entregar'), ('Entregado', 'Entregado')], max_length=50, null=True),
        ),
    ]
