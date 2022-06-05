# Generated by Django 3.2.13 on 2022-06-05 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinkoff', '0005_DolyameTypoFix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dolyamenotification',
            name='status',
            field=models.CharField(choices=[('approved', 'Approved'), ('rejected', 'Rejected'), ('refunded', 'Refunded'), ('canceled', 'Canceled'), ('committed', 'Committed'), ('wait_for_commit', 'Waiting for commit'), ('completed', 'Completed')], max_length=32),
        ),
    ]
