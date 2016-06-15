from django.db import models

# Create your models here.

class Personalinfo(models.Model):

	class Meta:
		verbose_name_plural = "Данные об абитуриенте"
		verbose_name = "данные об абитуриенте"

	'''personal_info'''
	surname = models.CharField(max_length=30, null = True, blank = True, verbose_name = "Фамилия")
	name = models.CharField(max_length=30, null = True, blank = True, verbose_name = "Имя")
	patronymic = models.CharField(max_length=30, null = True, blank = True, verbose_name = "Отчество")
	birth = models.DateField(null = True, blank = True, verbose_name = "Дата рождения")
	bpl = models.CharField(max_length=50, null = True, blank = True, verbose_name = "Место рождения")
	citizenship = models.CharField(max_length=70, null = True, blank = True, verbose_name = "Гражданство")
	nationality = models.CharField(max_length=30, null = True, blank = True, verbose_name = "Национальность")
	homephone = models.CharField(max_length = 20, null = True, blank = True, verbose_name = "Домашний телефон")
	mobilephone = models.PositiveSmallIntegerField(null = True, blank = True, verbose_name = "Мобильный телефон")
	registration = models.CharField(max_length=30, null = True, blank = True, verbose_name = "Прописка")
	address = models.CharField(max_length=30, null = True, blank = True, verbose_name = "Адрес проживания")
	'''passport_data'''
	series = models.PositiveSmallIntegerField(null = True, blank = True, verbose_name = "Серия паспорта")
	number = models.PositiveSmallIntegerField(null = True, blank = True, verbose_name = "Номер паспорта")
	issued = models.CharField(max_length=70, null = True, blank = True, verbose_name = "Кем выдан паспорт")
	issuance_date = models.DateField(null = True, blank = True, verbose_name = "Дата выдачи паспорта")
	'''parents_info'''
	m_surname = models.CharField(max_length=30, blank = True, null = True, verbose_name = "Фамилия матери")
	m_name = models.CharField(max_length=30, blank = True, null = True, verbose_name = "Имя матери")
	m_patronymic = models.CharField(max_length=30, blank = True, null = True, verbose_name = "Отчество матери")
	m_job = models.CharField(max_length=30, blank = True, null = True, verbose_name = "Работа матери")
	m_post = models.CharField(max_length=30, blank = True, null = True, verbose_name = "Должность матери")
	m_phone = models.CharField(max_length = 20, null = True, blank = True, verbose_name = "Телефон матери")
	f_surname = models.CharField(max_length=30, blank = True, null = True, verbose_name = "Фамилия отца")
	f_name = models.CharField(max_length=30, blank = True, null = True, verbose_name = "Имя отца")
	f_patronymic = models.CharField(max_length=30, blank = True, null = True, verbose_name = "Отчество отца")
	f_job = models.CharField(max_length=30, blank = True, null = True, verbose_name = "Работа отца")
	f_post = models.CharField(max_length=30, blank = True, null = True, verbose_name = "Должность отца")
	f_phone = models.CharField(max_length = 20, null = True, blank = True, verbose_name = "Телефон отца")
	'''education'''
	#education_lvl = models.CharField(max_length=35, null = True, blank = True, verbose_name = "Уровень образования")
	speciality = models.CharField(max_length=40, null = True, blank = True, verbose_name = "Выбранная специальность")
	finished_school = models.CharField(max_length=30, null = True, blank = True, verbose_name = "Законченная школа")
	date_finished = models.DateField(null = True, blank = True, verbose_name = "Дата окончания")
	#education_doc = models.CharField(max_length=30, null = True, blank = True, verbose_name = "Документ об образовании")
	'''requisites'''
	doc_series = models.PositiveSmallIntegerField(null = True, blank = True, verbose_name = "Серия документа об образовании")
	doc_number = models.PositiveSmallIntegerField(null = True, blank = True, verbose_name = "Номер документа об образовании")
	#math = models.CharField(max_length=30, null = True, blank = True, verbose_name = "")
	#russian = models.CharField(max_length=30, null = True, blank = True, verbose_name = "")
	prof_subj = models.CharField(max_length=30, null = True, blank = True, verbose_name = "")
	math_mark = models.PositiveSmallIntegerField(null = True, blank = True, verbose_name = "Оценка по математике")
	russian_mark = models.PositiveSmallIntegerField(null = True, blank = True, verbose_name = "Оценка по русскому языку")
	prof_subj_mark = models.PositiveSmallIntegerField(null = True, blank = True, verbose_name = "Оценка по профильному предмету")
	avg_mark = models.FloatField(null = True, blank = True, verbose_name = "Средний балл")
	#language = models.CharField(max_length=30, null = True, blank = True, verbose_name = "Изучаемый иностранный язык")

	def __str__(self):
		return self.surname + " " + self.name + " " + self.patronymic 
