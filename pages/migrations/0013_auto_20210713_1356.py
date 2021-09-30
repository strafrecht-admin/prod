# Generated by Django 3.2.5 on 2021-07-13 13:56

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtailmodelchooser.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20210712_0135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sessionpage',
            options={},
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='sidebar',
            field=wagtail.core.fields.StreamField([('sidebar_title', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock())])), ('sidebar_image_text', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('sidebar_poll', wagtail.core.blocks.StructBlock([('poll', wagtailmodelchooser.blocks.ModelChooserBlock(target_model='wagtailpolls.poll'))]))]),
        ),
        migrations.AlterField(
            model_name='sessionspage',
            name='content',
            field=wagtail.core.fields.StreamField([('content', wagtail.core.blocks.StreamBlock([('richtext', wagtail.core.blocks.RichTextBlock()), ('semester_block', wagtail.core.blocks.StructBlock([('semester', wagtail.core.blocks.ChoiceBlock(choices=[('ss2022', 'Sommersemester 2022'), ('ws2022', 'Wintersemester 2022'), ('ss2021', 'Sommersemester 2021'), ('ws2021', 'Wintersemester 2021'), ('ss2020', 'Sommersemester 2020'), ('ws2020', 'Wintersemester 2020'), ('ss2019', 'Sommersemester 2019'), ('ws2019', 'Wintersemester 2019'), ('ss2018', 'Sommersemester 2018'), ('ws2018', 'Wintersemester 2018')], icon='calendar'))]))]))]),
        ),
    ]
