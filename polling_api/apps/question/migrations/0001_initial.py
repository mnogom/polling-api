# Generated by Django 2.2.10 on 2022-04-28 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(error_messages={'blank': "Question text can't be empty", 'null': "Question text can't be empty"}, max_length=300)),
                ('type', models.SmallIntegerField(choices=[(1, 'Single choice'), (2, 'Multiple choices'), (3, 'Text answer')], default=3)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quiz.Quiz')),
            ],
            options={
                'verbose_name_plural': 'Questions',
            },
        ),
    ]