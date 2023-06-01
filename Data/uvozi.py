import pandas as pd
from pandas import DataFrame

from typing import Dict
from re import sub
import dataclasses


# Vse kar delamo z bazo se nahaja v razredu Repo.
from auth_public import *

import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki


conn = psycopg2.connect(database=db, host=host, user=user, password=password)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

def ustvari_sql_tabele():
    with open('Data/CREATE_TABLE.sql') as tabele:
        koda = tabele.read()
    cur.execute(koda)
    conn.commit()
    print('Uspešno ustvaril tabele!')

def dodaj_sql_podatke(detoteka):
    with open('podatki/{0}'.format(detoteka), encoding= 'utf-8') as sqlvrstice:
        koda = sqlvrstice.read()
        cur.execute(koda)
    conn.commit()
    print('Uspesno nalozil podatke!')


ustvari_sql_tabele()
dodaj_sql_podatke('uporabnik.sql')
dodaj_sql_podatke('turneja.sql')
#dodaj_sql_podatke('koncert.sql')
dodaj_sql_podatke('rezervacija.sql')
#dodaj_sql_podatke('ocena.sql')
