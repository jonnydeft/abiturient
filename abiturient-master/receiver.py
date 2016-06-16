# -*- coding: utf-8 -*-
import sqlite3
import sys
import codecs
import re
from odf.opendocument import load, OpenDocumentText
from odf.text import P
from odf import text, teletype
from reportlab import *
from ezodf import *
def getAndinsert(cur, counter):
    changeList = ['FamName',
                  'Name',
                  'Patron',
                  'BirDay',
                  'BirPlace',
                  'CitShip',
                  'Natio',
                  'HomePhone',
                  'MobPhone',
                  'Registr',
                  'Living',
                  'PassSer',
                  'PassNum',
                  'Whom',
                  'When',
                  'MothFname',
                  'MothName',
                  'MothPatr',
                  'MothPlace',
                  'MothPos',
                  'MothNum',
                  'FathFname',
                  'FathName',
                  'FathPatr',
                  'FathPlace',
                  'FathPos',
                  'FathNum',
                  'SpecDescr',
                  'EduName',
                  'EduEnd',
                  'EdSer',
                  'EdNum',
                  'FstNum',
                  'SecNum',
                  'ThrNum',
                  'ThrSub',
                  'GPA'
                 ]
    doc   = ezodf.opendoc('example.odt')
    for i in changeList:
        replaced = False
        for line in doc:
            print(line)
            if i in line:
                p = P(text = changeList)
                n = P(text = dataList[counter])
                line.replace(i, n)
                counter += 1
    doc.save('completed.odt')
    
'''Участок работы с базой данных'''
counter    = 0
enteredID  = input('Введите номер записи\n')
conn       = sqlite3.connect('db.sqlite3')
c          = conn.cursor()
cur        = c.execute('select surname, name, patronymic, birth, bpl, citizenship, nationality, homephone, mobilephone, registration, address, series, number, issued, issuance_date, m_surname, m_name, m_patronymic, m_job, m_post, m_phone, f_surname, f_name, f_patronymic, f_job, f_post, f_phone, speciality, finished_school, date_finished, doc_series, doc_number, math_mark, russian_mark, prof_subj_mark, prof_subj, avg_mark from abiturient_personalinfo where id=%s' % enteredID)


'''Создание списка из записи таблицы'''
dataList   = []
for row in cur:
    dataList = str(row).split(',')
    
getAndinsert(dataList, counter)
