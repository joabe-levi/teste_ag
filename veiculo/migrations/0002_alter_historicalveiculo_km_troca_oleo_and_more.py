# Generated by Django 4.2.11 on 2024-04-18 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalveiculo',
            name='km_troca_oleo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Quilometros até a próxima troca'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='km_troca_oleo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Quilometros até a próxima troca'),
        ),
    ]
