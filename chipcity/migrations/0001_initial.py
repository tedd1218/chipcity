# Generated by Django 5.0.1 on 2024-04-18 20:00

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
                ('is_big_blind', models.BooleanField(default=False)),
                ('is_small_blind', models.BooleanField(default=False)),
                ('is_all_in', models.BooleanField(default=False)),
                ('current_bet', models.IntegerField(default=0, null=True)),
                ('can_check', models.BooleanField(default=False)),
                ('can_raise', models.BooleanField(default=True)),
                ('can_call', models.BooleanField(default=True)),
                ('most_recent_action', models.CharField(blank=True, max_length=50, null=True)),
                ('card_left', models.IntegerField(default=0, null=True)),
                ('card_right', models.IntegerField(default=0, null=True)),
                ('hand_is_active', models.BooleanField(default=True)),
                ('win_count', models.IntegerField(default=0, null=True)),
                ('winning_hand', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='player', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_num', models.IntegerField(null=True)),
                ('players_connected', models.IntegerField(default=0)),
                ('num_players_with_active_hand', models.IntegerField(default=0)),
                ('total_pot', models.IntegerField(default=0)),
                ('flop1', models.IntegerField(default=0)),
                ('flop2', models.IntegerField(default=0)),
                ('flop3', models.IntegerField(default=0)),
                ('turn', models.IntegerField(default=0)),
                ('river', models.IntegerField(default=0)),
                ('curr_round', models.IntegerField(default=0)),
                ('highest_curr_bet', models.IntegerField(default=0)),
                ('last_raise', models.IntegerField(default=0)),
                ('last_action', models.IntegerField(default=0)),
                ('big_blind_amt', models.IntegerField(default=2)),
                ('small_blind_amt', models.IntegerField(default=1)),
                ('winning_player_user', models.CharField(blank=True, max_length=100, null=True)),
                ('big_blind_player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='big_blind_player', to='chipcity.player')),
                ('current_player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='current_player', to='chipcity.player')),
                ('small_blind_player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='small_blind_player', to='chipcity.player')),
            ],
        ),
    ]
