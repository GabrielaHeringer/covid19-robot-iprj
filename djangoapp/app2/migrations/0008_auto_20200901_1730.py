# Generated by Django 3.0.5 on 2020-09-01 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0007_avisoporemail_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='avisoporemail',
            name='autor',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='avisoporemail',
            name='busca_global',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='avisoporemail',
            name='button_autores',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='avisoporemail',
            name='button_titulo_e_resumo',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='avisoporemail',
            name='idiomas',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='avisoporemail',
            name='opcao_titulo_resumo',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='avisoporemail',
            name='titulo_e_resumo',
            field=models.TextField(blank=True),
        ),
    ]