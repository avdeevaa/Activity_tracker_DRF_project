# Generated by Django 5.0.2 on 2024-02-09 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(choices=[('home', 'home'), ('outside', 'outside'), ('work', 'work')], default='home', verbose_name='место для привычки')),
                ('time', models.DateTimeField(verbose_name='время для привычки')),
                ('action', models.CharField(max_length=500, verbose_name='действие привычки')),
                ('is_enjoyable_action', models.BooleanField(blank=True, default=False, null=True, verbose_name='Признак приятной привычки')),
                ('is_useful_action', models.BooleanField(blank=True, default=False, null=True, verbose_name='Связанная, полезная привычка')),
                ('periodicity', models.CharField(choices=[('daily', 'daily'), ('once a week', 'once a week'), ('twice a week', 'twice a week')], default='daily', verbose_name='Периодичность')),
                ('reward', models.CharField(max_length=500, verbose_name='Вознаграждение')),
                ('activity_time', models.PositiveIntegerField(verbose_name='Время на выполнение')),
                ('public', models.BooleanField(default=False, verbose_name='Признак публичности')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]
