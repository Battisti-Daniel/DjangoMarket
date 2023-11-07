# Generated by Django 4.2.7 on 2023-11-07 18:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('AccountManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketRoles',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('accessibility', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AccountManagement.marketroles'),
        ),
    ]
