# Generated by Django 3.0.5 on 2020-05-28 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assunto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('palavrasChaves', models.TextField()),
                ('dataInclusao', models.DateField()),
                ('stringBusca', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Credibilidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Especialista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField()),
                ('especialidade', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pesquisador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PortalBusca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField()),
                ('dataInclusao', models.DateField(auto_now_add=True)),
                ('descricao', models.TextField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Novidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataPrimeiroAcesso', models.DateField(auto_now_add=True)),
                ('idioma', models.TextField()),
                ('resumo', models.TextField(blank=True)),
                ('autores', models.TextField(blank=True)),
                ('fonte', models.URLField()),
                ('link_externo', models.URLField(blank=True)),
                ('jornal', models.TextField(blank=True)),
                ('titulo', models.CharField(max_length=250, unique=True)),
                ('categoria', models.TextField(blank=True)),
                ('data_publicacao', models.TextField(blank=True)),
                ('credibilidade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Credibilidade')),
                ('especialista', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Especialista')),
                ('portalBusca', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.PortalBusca')),
            ],
        ),
        migrations.CreateModel(
            name='AvisoPorEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataInicialRecebim', models.DateField()),
                ('dataFinalRecebim', models.DateField()),
                ('poisNovidade', models.TextField()),
                ('assuntoAviso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Assunto')),
                ('credibilidadeAviso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Credibilidade')),
                ('pesquisador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pesquisador')),
            ],
        ),
        migrations.AddField(
            model_name='assunto',
            name='novidade',
            field=models.ManyToManyField(to='app.Novidade'),
        ),
    ]
