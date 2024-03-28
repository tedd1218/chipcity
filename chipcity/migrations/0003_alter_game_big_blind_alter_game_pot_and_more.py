# Generated by Django 5.0.1 on 2024-03-28 17:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chipcity', '0002_remove_profile_user_game_dealer_game_num_of_players_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='big_blind',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='big_blind', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='game',
            name='pot',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='game',
            name='small_blind',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='small_blind', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='game',
            name='table_num',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='table_num', to=settings.AUTH_USER_MODEL),
        ),
    ]
