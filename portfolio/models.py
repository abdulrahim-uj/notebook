import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class About(models.Model):
    tbl_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title_one = models.CharField(max_length=128, blank=True)
    title_two = models.CharField(max_length=128, blank=True)
    title_three = models.CharField(max_length=128, blank=True)
    title_four = models.CharField(max_length=128, blank=True)
    content_one = models.CharField(max_length=1000, blank=True)
    content_two = models.CharField(max_length=1000, blank=True)
    content_three = models.CharField(max_length=1000, blank=True)
    images = models.ImageField(upload_to='portfolio/about/', blank=True)
    date_added = models.DateTimeField(db_index=True, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_port_about'
        verbose_name = _('portfolio About')
        verbose_name_plural = _('portfolio Abouts')
        ordering = ('date_added',)

    def __unicode__(self):
        return self.tbl_id


class Ulli(models.Model):
    tbl_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ul_name = models.CharField(max_length=50, blank=True)
    li_data = models.CharField(max_length=1000)
    date_added = models.DateTimeField(db_index=True, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_port_ulli'
        verbose_name = _('Portfolio Ulli')
        verbose_name_plural = _('Portfolio Ullis')
        ordering = ('date_added',)

    def __unicode__(self):
        return self.tbl_id


class Experience(models.Model):
    tbl_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(db_index=True, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    section = models.CharField(max_length=128, blank=True)
    heading = models.CharField(max_length=128, blank=True)
    sub_head = models.CharField(max_length=128, blank=True)
    date_from = models.DateField(blank=True)
    date_to = models.DateField(blank=True)
    story = models.TextField(blank=True)
    story_sub = models.TextField(blank=True)
    image_files = models.ImageField(upload_to='portfolio/experience/', blank=True)
    link_texts = models.CharField(max_length=128, blank=True)

    class Meta:
        db_table = 'tbl_port_experience'
        verbose_name = _('portfolio Experience')
        verbose_name_plural = _('portfolio Experiences')
        ordering = ('date_added',)

    def __unicode__(self):
        return self.tbl_id


class Contact(models.Model):
    tbl_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(db_index=True, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    air_name = models.CharField(max_length=128)
    air_email = models.EmailField()
    air_phone = models.CharField(max_length=13)
    air_subject = models.CharField(max_length=128)
    air_message = models.CharField(max_length=1000)

    class Meta:
        db_table = 'tbl_port_contact'
        verbose_name = _('Portfolio Contact')
        verbose_name_plural = _('Portfolio Contacts')
        ordering = ('date_added',)

    def __unicode__(self):
        return self.tbl_id
