# Generated by Django 3.2.5 on 2023-02-02 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0004_auto_20230202_1619'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deck',
            options={'verbose_name': 'Flashcard-Deck'},
        ),
        migrations.AlterField(
            model_name='flashcard',
            name='deck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flashcards', to='flashcards.deck'),
        ),
    ]
