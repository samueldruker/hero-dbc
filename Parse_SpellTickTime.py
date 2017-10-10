# -*- coding: utf-8 -*-
# pylint: disable=C0103
# pylint: disable=C0301

"""
@author: Kutikuti
"""

import sys
import os
import csv

generatedDir = os.path.join('DBC', 'generated')
parsedDir = os.path.join('DBC', 'parsed')

os.chdir(os.path.join(os.path.dirname(sys.path[0]), 'AethysDBC'))

with open(os.path.join(generatedDir, 'SpellEffect.csv')) as csvfile:
    reader = list(csv.DictReader(csvfile, escapechar='\\'))
    with open(os.path.join(parsedDir, 'TickTime.lua'), 'w', encoding='utf-8') as file:
        file.write('AethysCore.Enum.TickTime = {\n')
        for i, row in enumerate(reader):
            if not row['amplitude'] == "0" :
                file.write('  [' + row['id_spell'] + '] = ' + str(int(row['amplitude'])) + ',\n')
        file.write('}\n')