# Generated by Django 5.0.1 on 2024-04-17 14:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet', models.IntegerField(default=100, null=True)),
                ('chips', models.IntegerField(default=50, null=True)),
                ('seat_number', models.IntegerField(default=0, null=True)),
                ('content_type', models.CharField(blank=True, max_length=50, null=True)),
                ('is_participant', models.BooleanField(default=True)),
                ('is_big_blind', models.BooleanField(default=True)),
                ('is_small_blind', models.BooleanField(default=True)),
                ('is_all_in', models.BooleanField(default=False)),
                ('current_bet', models.IntegerField(default=0, null=True)),
                ('can_check', models.BooleanField(default=True)),
                ('can_raise', models.BooleanField(default=True)),
                ('can_call', models.BooleanField(default=True)),
                ('most_recent_action', models.CharField(blank=True, max_length=50, null=True)),
                ('card_left', models.CharField(max_length=20)),
                ('card_right', models.CharField(max_length=20)),
                ('hand_is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='player', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_num', models.IntegerField(null=True)),
                ('players_connected', models.IntegerField(default=0)),
                ('total_pot', models.IntegerField(default=0)),
                ('flop1', models.CharField(max_length=20, null=True)),
                ('flop2', models.CharField(max_length=20, null=True)),
                ('flop3', models.CharField(max_length=20, null=True)),
                ('turn', models.CharField(max_length=20, null=True)),
                ('river', models.CharField(max_length=20, null=True)),
                ('curr_round', models.IntegerField(default=0)),
                ('highest_curr_bet', models.IntegerField(default=0)),
                ('last_raise', models.IntegerField(default=0)),
                ('last_action', models.IntegerField(default=0)),
                ('big_blind_amt', models.IntegerField(default=2)),
                ('small_blind_amt', models.IntegerField(default=1)),
                ('big_blind_player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='big_blind_player', to='chipcity.player')),
                ('current_player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='current_player', to='chipcity.player')),
                ('small_blind_player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='small_blind_player', to='chipcity.player')),
            ],
        ),
    ]
