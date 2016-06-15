# -*- coding: utf-8 -*-
import sqlite3
import sys
import re
import codecs
import io
from pdfgen import *
from reportlab import *

conn       = sqlite3.connect('db.sqlite3')
#exampleODT = open('example.odt', 'rb')
#for line in exampleODT:
    #print(line.decode('utf8'))
#exampleODT.read()

#with open('example.odt', mode='a', encoding='utf8') as f:
 #   while index != (count_index - offset_index):
  #      f.write(str(search_result[index + 1]))
   #     f.write('\n')
    #    index += 1

word = u'привет'
with io.open('example.odt', encoding='utf-8') as file:
    for line in file:
        if word in line:
            print(line, end='')

c          = conn.cursor()
enteredID  = input('Введите номер записи\n')
cur        = c.execute('select surname, name, patronymic, birth, bpl, citizenship, nationality, homephone, mobilephone, registration, address, series, number, issued, issuance_date, m_surname, m_name, m_patronymic, m_job, m_post, m_phone, f_surname, f_name, f_patronymic, f_job, f_post, f_phone, speciality, finished_school, date_finished, doc_series, doc_number, math_mark, russian_mark, prof_subj_mark, avg_mark from abiturient_personalinfo where id=%s' % enteredID)

for row in cur:
    getAndinsert(exampleODT, cur)
 
