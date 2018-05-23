# Generated by Django 2.0 on 2018-05-22 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GameData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='StatData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.FloatField()),
                ('traffic', models.FloatField()),
                ('crime', models.FloatField()),
                ('population', models.IntegerField()),
                ('money', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='StateData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='states', to='game.AgentData')),
                ('stats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state', to='game.StatData')),
            ],
        ),
        migrations.CreateModel(
            name='TechData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schools', models.IntegerField()),
                ('curriculum', models.IntegerField()),
                ('roads', models.IntegerField()),
                ('infrastructure', models.IntegerField()),
                ('police_stations', models.IntegerField()),
                ('police_training', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='statedata',
            name='tech',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state', to='game.TechData'),
        ),
        migrations.AddField(
            model_name='gamedata',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='game.User'),
        ),
        migrations.AddField(
            model_name='agentdata',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agents', to='game.GameData'),
        ),
    ]
