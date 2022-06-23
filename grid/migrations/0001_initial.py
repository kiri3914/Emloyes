# Generated by Django 4.0.5 on 2022-06-23 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(max_length=55)),
                ('image', models.ImageField(upload_to='employers/')),
                ('stack', models.CharField(blank=True, max_length=1000, null=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=244, null=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('visited', models.BooleanField(choices=[(True, 'Посетил(а)'), (False, 'Отсутствовал(а)')])),
                ('time_start', models.TimeField(blank=True, default='00:00', null=True)),
                ('time_end', models.TimeField(blank=True, default='00:00', null=True)),
                ('reason', models.CharField(blank=True, default='-----', max_length=100, null=True)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grid.employee')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grid.position'),
        ),
    ]
