# Generated by Django 3.0.8 on 2021-01-06 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_seeded_manage_cand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidatePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_name', models.CharField(blank=True, max_length=100)),
                ('image_name', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='candidate',
            name='details',
            field=models.TextField(blank=True, default=''),
        ),
    ]