# -*- coding: utf-8 -*- 
import re
from reportlab import *

def getAndinsert(exampleODT, cur):
    value      = 1
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
    for i in changeList:
        re.sub(changeList[value], cur, exampleODT)
        value =+ 1
