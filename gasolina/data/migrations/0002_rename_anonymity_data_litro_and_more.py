# Generated by Django 4.0.2 on 2022-03-02 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='anonymity',
            new_name='litro',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='city',
            new_name='tempo_ultima_venda',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='ip_address',
            new_name='ultima_venda',
        ),
        migrations.RemoveField(
            model_name='data',
            name='country',
        ),
        migrations.RemoveField(
            model_name='data',
            name='port',
        ),
        migrations.RemoveField(
            model_name='data',
            name='protocol',
        ),
        migrations.RemoveField(
            model_name='data',
            name='region',
        ),
        migrations.RemoveField(
            model_name='data',
            name='response',
        ),
        migrations.RemoveField(
            model_name='data',
            name='transfer',
        ),
        migrations.RemoveField(
            model_name='data',
            name='uptime',
        ),
        migrations.AddField(
            model_name='data',
            name='local',
            field=models.CharField(blank=True, max_length=55),
        ),
        migrations.AddField(
            model_name='data',
            name='nome_intituicao',
            field=models.CharField(blank=True, max_length=35),
        ),
        migrations.AddField(
            model_name='data',
            name='titulo',
            field=models.CharField(blank=True, max_length=35),
        ),
    ]
