from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from modelcluster.fields import ParentalKey

class JurcoachCarousel(Orderable):
    page = ParentalKey('pages.JurcoachPage', related_name='jurcoachcarousel')
    illustration_choices = [
        ('falltraining', 'Falltraining'),
        ('wiki', 'Problemfeldwiki'),
        ('mct', 'Multiple-Choice-Test'),
        ('klausurdatenbank', 'Klausurdatenbank'),
        ('rechtsprechung', 'Höchstrichterliche Rechtsprechung'),
    ]
    illustration = models.CharField(
        choices=illustration_choices,
        max_length=255,
        blank=True
    )
    carousel_headline = models.CharField(max_length=200, null=True, blank=True)
    carousel_description = RichTextField(null=True, blank=True)
    carousel_link_text = models.CharField(max_length=200, null=True, blank=True)

    panels = [FieldPanel('illustration', classname="col-12"),
             FieldPanel('carousel_headline', classname="col-12"),
             FieldPanel('carousel_description', classname="col-12"),
             FieldPanel('carousel_link_text', classname="col-12"),]

class JurcoachPage(Page):
    body = RichTextField(blank=True)
    header = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('header'),
        MultiFieldPanel(
            [InlinePanel('jurcoachcarousel', max_num=10, min_num=0, label='Slide1')],
            heading='Slider',
        ),
    ]
    
