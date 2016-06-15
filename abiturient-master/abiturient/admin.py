from django.contrib import admin

from .models import Personalinfo

# Register your models here.

class PersonalInfoAdmin(admin.ModelAdmin):
    fieldsets = [
            ('Ваши личные данные', {'fields': ['surname', 'name', 'patronymic', 'birth', 'bpl', 'citizenship', 'nationality', 'homephone', 'mobilephone', 'registration', 'address']}),
            ('Паспортные данные', {'fields': ['series', 'number', 'issued', 'issuance_date']}),
            ('Данные Ваших родителей', {'fields': ['m_surname', 'm_name', 'm_patronymic', 'm_job', 'm_post', 'm_phone', 'f_surname', 'f_name', 'f_patronymic', 'f_job', 'f_post', 'f_phone']}),
            ('Ваше текущее образование', {'fields': ['speciality', 'finished_school', 'date_finished']}),
            ('Реквизиты документа об образовании', {'fields': ['doc_series', 'doc_number']}),
            ('Отметки', {'fields': ['math_mark', 'russian_mark', 'prof_subj_mark', 'avg_mark']}),
    ]

admin.site.register(Personalinfo, PersonalInfoAdmin)
