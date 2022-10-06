# Generated by Django 3.2.5 on 2022-10-06 14:22

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('birdsong', '0005_alter_receipt_success'),
    ]

    operations = [
        migrations.CreateModel(
            name='LSHNewsletter',
            fields=[
                ('campaign_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='birdsong.campaign')),
                ('body', wagtail.core.fields.StreamField([('rich_text', wagtail.core.blocks.RichTextBlock(features=['h3', 'h4', 'bold', 'italic', 'link', 'ul', 'ol', 'document-link'], template='birdsong/mail/blocks/richtext.html'))])),
            ],
            bases=('birdsong.campaign',),
        ),
        migrations.CreateModel(
            name='NewsletterEmail',
            fields=[
                ('campaign_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='birdsong.campaign')),
                ('body', wagtail.core.fields.StreamField([('rich_text', wagtail.core.blocks.RichTextBlock(features=['h3', 'h4', 'bold', 'italic', 'link', 'ul', 'ol', 'document-link'], template='birdsong/mail/blocks/richtext.html'))])),
            ],
            bases=('birdsong.campaign',),
        ),
    ]
