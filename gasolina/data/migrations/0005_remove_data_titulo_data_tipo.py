# Generated by Django 4.0.3 on 2022-03-04 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_remove_data_nome_intituicao_data_nome_empresa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='titulo',
        ),
        migrations.AddField(
            model_name='data',
            name='tipo',
            field=models.CharField(blank=True, max_length=55),
        ),
    ]
