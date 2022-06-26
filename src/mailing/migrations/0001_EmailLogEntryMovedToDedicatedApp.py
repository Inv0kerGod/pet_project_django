# Generated by Django 3.2.13 on 2022-06-25 10:40

from django.db import migrations, models


def migrate_from_previous_table(apps, schema_editor):
    """This is a bit weird way to migrate models between apps,

    but right now i am completely offline and this code is way much better then no code
    """
    EmailLogEntry = apps.get_model('mailing.EmailLogEntry')

    previous_entries = apps.get_model('app.EmailLogEntry').objects.values(
        'modified',
        'email',
        'template_id',
    )

    EmailLogEntry.objects.bulk_create([EmailLogEntry(**entry) for entry in previous_entries])  # actualy loosing message send times here, flex scope


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0003_RenameCoursesAppPt1'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailLogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('email', models.CharField(max_length=255)),
                ('template_id', models.CharField(max_length=255)),
            ],
            options={
                'unique_together': {('email', 'template_id')},
                'index_together': {('email', 'template_id')},
            },
        ),
        migrations.RunPython(migrate_from_previous_table),
    ]
