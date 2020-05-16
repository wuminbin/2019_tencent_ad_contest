# coding: utf-8

import sqlite3

import pandas as pd

from constants import DATA_DIR, HEADER_USER

con = sqlite3.connect(DATA_DIR + 'user.db')
con.execute('create index value_index on user(value);')
con.commit()

