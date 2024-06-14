# Generated by Django 3.2.5 on 2023-02-07 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tandem_exams.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TandemExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('difficulty', models.CharField(choices=[('beginner', 'beginner'), ('advanced', 'advanced')], max_length=100)),
                ('description', models.TextField(default='')),
                ('approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tandemklausur',
                'verbose_name_plural': 'Tandemklausuren',
            },
        ),
        migrations.CreateModel(
            name='ExamSolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to=tandem_exams.models.ExamSolution.file_target)),
                ('correction', models.FileField(blank=True, null=True, upload_to=tandem_exams.models.ExamSolution.correction_target)),
                ('correction_sheet', models.FileField(blank=True, null=True)),
                ('state', models.CharField(choices=[('NEW', 'new'), ('ACCEPTED', 'accepted'), ('CORRECTED', 'corrected')], default='NEW', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('correction_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exam_solution_corrections', to=settings.AUTH_USER_MODEL)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='tandem_exams.tandemexam')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_solutions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Klausurlösung',
                'verbose_name_plural': 'Klausurlösungen',
            },
        ),
    ]
