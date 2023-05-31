from django.core.exceptions import MultipleObjectsReturned, ValidationError
from django.db.models.deletion import SET_NULL
from data.models import *
import csv
import datetime
import re
import sys
import string

#path = sys.argv[1] 
#argv_nama_wilayah = sys.argv[2]
path = 'result.csv'

with open(path) as f:
    reader = csv.reader(f,delimiter=';')

    for row in reader:
        print(row[0], row[1])
