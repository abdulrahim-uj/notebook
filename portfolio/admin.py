from django.contrib import admin
from portfolio.models import About, Ulli, Experience, Contact


class AboutAdmin(admin.ModelAdmin):
    list_display = ('tbl_id', 'title_one', 'title_two', 'title_three', 'title_four',
                    'content_one', 'content_two', 'content_three', 'images', 'date_added', 'date_updated')


admin.site.register(About, AboutAdmin)


class UlliAdmin(admin.ModelAdmin):
    list_display = ('tbl_id', 'ul_name', 'li_data', 'date_added', 'date_updated')


admin.site.register(Ulli, UlliAdmin)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('tbl_id', 'section', 'heading', 'sub_head', 'date_from',
                    'date_to', 'story', 'story_sub', 'image_files', 'link_texts', 'date_added', 'date_updated')


admin.site.register(Experience, ExperienceAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('tbl_id', 'air_name', 'air_email', 'air_phone', 'air_subject', 'air_message', 'date_added', 'date_updated')


admin.site.register(Contact, ContactAdmin)
