# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 08:39:42 2022

@author: usuario
"""

#fecha y hora

from datetime import datetime

fechayhora = datetime.now()

print(f" Hoy: {fechayhora}")
print(fechayhora.year)
print(fechayhora.month)
print(fechayhora.day)
print(fechayhora.hour)
print(fechayhora.minute)
print(fechayhora.second)
print(fechayhora.microsecond)