# Generated by Django 2.2.6 on 2021-06-04 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_add_domain_domain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_domain',
            name='Donain_name',
        ),
        migrations.AddField(
            model_name='add_domain',
            name='add_domain',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='add_domain',
            name='donain',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mainpage.Domain'),
        ),
    ]
