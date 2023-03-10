# Generated by Django 4.1.4 on 2023-02-09 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('word', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Synonym',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('similar', models.CharField(blank=True, max_length=200, null=True)),
                ('word', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.word')),
            ],
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('sentence', models.CharField(blank=True, max_length=300, null=True)),
                ('word', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.word')),
            ],
        ),
        migrations.CreateModel(
            name='Pharase',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('sentence', models.CharField(blank=True, max_length=400, null=True)),
                ('word', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.word')),
            ],
        ),
        migrations.CreateModel(
            name='Meaning',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('meaning', models.CharField(blank=True, max_length=200, null=True)),
                ('word', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.word')),
            ],
        ),
        migrations.CreateModel(
            name='Antononym',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('opposite', models.CharField(blank=True, max_length=200, null=True)),
                ('word', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.word')),
            ],
        ),
    ]
