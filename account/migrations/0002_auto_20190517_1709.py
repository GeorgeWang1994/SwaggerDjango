# Generated by Django 2.2.1 on 2019-05-17 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apipermission',
            name='role',
            field=models.CharField(choices=[('SUPER', 'SUPER'), ('ADMIN', 'ADMIN'), ('USER', 'USER')], default='USER', max_length=10, verbose_name='权限的角色'),
        ),
        migrations.AlterField(
            model_name='apiuser',
            name='role',
            field=models.CharField(choices=[('SUPER', 'SUPER'), ('ADMIN', 'ADMIN'), ('USER', 'USER')], default='ADMIN', max_length=10, verbose_name='用户角色'),
        ),
    ]
