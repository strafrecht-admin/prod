# Generated by Django 3.2.5 on 2021-07-26 17:24

from django.db import migrations, models
import django.db.models.deletion
import wagtail.contrib.routable_page.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail_color_panel.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('pages', '0015_auto_20210726_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('content', wagtail.core.fields.StreamField([('content', wagtail.core.blocks.StreamBlock([('richtext', wagtail.core.blocks.RichTextBlock()), ('events_block', wagtail.core.blocks.StructBlock([]))]))])),
                ('sidebar', wagtail.core.fields.StreamField([('sidebar_title', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock())])), ('sidebar_header', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('color', wagtail_color_panel.blocks.NativeColorBlock('color', default='#333d44')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('content', wagtail.core.blocks.RichTextBlock(required=False))])), ('sidebar_border', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock())])), ('sidebar_simple', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock())])), ('sidebar_image_text', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]))], blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
    ]