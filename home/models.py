# from django.db import models
# from wagtail.admin.edit_handlers import FieldPanel
# from wagtail.core.fields import RichTextField
# from wagtail.core.models import Page
#
#
# class HomePage(Page):
#     templates="home/home_page.html"
#     max_count=1
#     banner_title=models.CharField(max_length=100, blank=False, null=True)
#     banner_subtitle=RichTextField(features=["bold", "italic"])
#     banner_image=models.ForeignKey(
#     "wagtailimages.Image",
#         null=True,
#         blank=False,
#         on_delete=models.SET_NULL,
#         related_name="+"
#     )
#
#     banner_cta=models.ForeignKey(
#
#         "wagtailcore.Page",
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name="+"
#     )
#
#     content_panels=Page.content_panels+[
#         FieldPanel("banner_title")
#     ]
#
#     class Meta:
#         verbose_name = "Home Page"
#         verbose_name_plural = "Home Pages"
# from django.db import models
#
# from wagtail.core.models import Page
# from wagtail.core.fields import RichTextField
# from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
# from wagtail.images.edit_handlers import ImageChooserPanel
#
#
# class HomePage(Page):
#     """Home page model."""
#
#     template = "home/home_page.html"
#     max_count = 1
#
#     banner_title = models.CharField(max_length=100, blank=False, null=True)
#     banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
#     banner_cta = models.ForeignKey(
#         "wagtailcore.Page",
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name="+"
#    )
#
#     content_panels = Page.content_panels + [
#         FieldPanel("banner_title"),
#         FieldPanel("banner_subtitle"),
#         ImageChooserPanel("banner_image"),
#         PageChooserPanel("banner_cta")
#     ]
#
#
#
#     class Meta:
#
#         verbose_name = "Home Page"
#         verbose_name_plural = "Home Pages"


from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock


class BlogPage(Page):
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], null=True,
        blank=True,

    )

    template = 'home/templates/home/home_page.html'

    content_panels = Page.content_panels+[
        FieldPanel('author'),
        FieldPanel('date'),
        StreamFieldPanel('body'),
    ]
