# Generated by Django 5.0 on 2024-02-29 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_address_customuser_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='confirm_password',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
