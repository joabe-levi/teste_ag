# Generated by Django 4.2.11 on 2024-04-18 00:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de criação')),
                ('data_modificacao', models.DateTimeField(auto_now=True, null=True, verbose_name='Data de modificação')),
                ('origem_dados', models.IntegerField(blank=True, choices=[(1, 'Manual'), (2, 'Importado'), (3, 'Sistema')], default=1, null=True, verbose_name='Origem dos dados')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('cod_motorista', models.CharField(max_length=50, verbose_name='Código do motorista')),
                ('nome', models.CharField(max_length=300, verbose_name='Nome')),
                ('telefone', models.CharField(blank=True, max_length=300, null=True, verbose_name='Telefone')),
                ('cnh', models.CharField(blank=True, max_length=300, null=True, verbose_name='Carteira Nacional de Habilitação')),
            ],
            options={
                'verbose_name': 'Motorista',
                'verbose_name_plural': 'Motoristas',
                'db_table': 'motorista',
            },
        ),
        migrations.CreateModel(
            name='HistoricalMotorista',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, verbose_name='UUID')),
                ('data_criacao', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Data de criação')),
                ('data_modificacao', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Data de modificação')),
                ('origem_dados', models.IntegerField(blank=True, choices=[(1, 'Manual'), (2, 'Importado'), (3, 'Sistema')], default=1, null=True, verbose_name='Origem dos dados')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('cod_motorista', models.CharField(max_length=50, verbose_name='Código do motorista')),
                ('nome', models.CharField(max_length=300, verbose_name='Nome')),
                ('telefone', models.CharField(blank=True, max_length=300, null=True, verbose_name='Telefone')),
                ('cnh', models.CharField(blank=True, max_length=300, null=True, verbose_name='Carteira Nacional de Habilitação')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Motorista',
                'verbose_name_plural': 'historical Motoristas',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]