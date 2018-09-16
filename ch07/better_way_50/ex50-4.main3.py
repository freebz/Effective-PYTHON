# main3.py
from analysis.utils import inspect as analisys_inspect
from frontend.utils import inspect as frontend_inspect

value = 33
if analisys_inspect(value) == frontend_inspect(value):
    print('Inspection equal!')
