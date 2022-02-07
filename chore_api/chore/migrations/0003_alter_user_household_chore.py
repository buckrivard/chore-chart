# Generated by Django 4.0.2 on 2022-02-07 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chore', '0002_remove_household_starter_list_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='household',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='chore.household'),
        ),
        migrations.CreateModel(
            name='Chore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('notes', models.TextField(null=True)),
                ('priority', models.PositiveSmallIntegerField()),
                ('done', models.BooleanField()),
                ('doer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chores', to='chore.user')),
                ('household', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chores', to='chore.household')),
            ],
        ),
    ]
