# Generated by Django 3.2.5 on 2022-10-25 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0028_auto_20220927_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='role',
            field=models.CharField(blank=True, choices=[('chairholder', 'Lehrstuhlinhaber'), ('office-management', 'Office Management'), ('academic-staff-male', 'Wiss. Mitarbeiter'), ('academic-staff-female', 'Wiss. Mitarbeiterin'), ('former academic-staff-male', 'Ehem. Wiss. Mitarbeiter'), ('former academic-staff-female', 'Ehem. Wiss. Mitarbeiterin'), ('academic-assistant', 'Wiss. Hilfskraft'), ('student-assistant', 'Stud. Hilfskraft'), ('jurcoach-law-team-academic', 'Wiss. Hilfskraft Jurcoach'), ('jurcoach-law-team-student', 'Stud. Hilfskraft Jurcoach'), ('jurcoach-evaluation-team', 'Jurcoach Evaluations-Team'), ('jurcoach-web-team', 'Jurcoach Informatik-Team'), ('webmaster', 'Webmaster'), ('associate-professor', 'Privatdozent')], max_length=255, verbose_name='Rolle'),
        ),
    ]