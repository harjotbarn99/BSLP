# Generated by Django 3.0.8 on 2021-01-06 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_seeded_manage_cand', '0002_auto_20210106_0438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidatephoto',
            old_name='candidate_name',
            new_name='venture_name',
        ),
    ]
