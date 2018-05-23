# Generated by Django 2.0 on 2018-05-22 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statedata',
            name='game',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='states', to='game.GameData'),
            preserve_default=False,
        ),
    ]
