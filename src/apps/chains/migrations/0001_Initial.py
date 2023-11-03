# Generated by Django 3.2.12 on 2022-03-16 19:16

from django.db import migrations
from django.db import models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0019_CourseDisplayInLMS'),
        ('studying', '0002_StudyIsHomeworkAccepted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('name', models.CharField(max_length=256, unique=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.course')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('name', models.CharField(max_length=256, unique=True)),
                ('template_id', models.CharField(max_length=256)),
                ('delay', models.BigIntegerField(default=0, verbose_name='Delay (minutes)')),
                ('chain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chains.chain')),
                ('parent', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL, to='chains.message')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chains.message')),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studying.study')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]