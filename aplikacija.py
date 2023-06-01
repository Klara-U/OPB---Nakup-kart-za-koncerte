# bottle
from bottleext import *
from bottle import *

# avtorizacija za priklop na bazo
from Data import auth_public as auth
# za gesla 
import hashlib
# za trenutni čas
from datetime import date
# za priklop na bazo
import psycopg2, psycopg2.extensions, psycopg2.extras
# znebimo se podatka s šumniki
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
import inspect
from functools import wraps

import os
# privzete nastavitve
SERVER_PORT = os.environ.get('BOTTLE_PORT', 8080)
RELOADER = os.environ.get('BOTTLE_RELOADER', True)
DB_PORT = os.environ.get('POSTGRES_PORT', 5432)

# priklop na bazo
conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password, port=DB_PORT)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#debug(True)


# pomožna funkcija za kodiranje gesel
def kodiranje_gesel(password):
    m = hashlib.sha256()
    m.update(password.encode("utf-8"))
    return m.hexdigest()

def zahtevan_cookie_uporabnik(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        cookie = request.get_cookie("uporabnik")
        if cookie:
            return f(*args, **kwargs)
        return template("prijava_uporabnik.html", napaka="Potrebna je prijava!")
    return decorated

@get('/static/<filename:path>')
def static(filename):
    return static_file(filename, root='static')

########################## PRIJAVA IN ODJAVA

@post('/prijava_uporabnik')
def prijava_uporabnik():
    uporabnisko_ime = request.forms.get('uporabnisko_ime')
    geslo = request.forms.get('geslo')

    if not auth.obstaja_uporabnik(uporabnisko_ime):
        return template("prijava_uporabnik.html", napaka = "Uporabnik s tem imenom ne obstaja!")
    prijava = auth.prijavi_uporabnika(uporabnisko_ime, geslo)
    if prijava:
        response.set_cookie("uporabnik", uporabnisko_ime)
        response.set_cookie("rola", prijava.role)

        redirect(url('index'))
    else:
        return template("prijava_uporabnik.html", napaka="Neuspešna prijava. Napačno geslo ali uporabniško ime.")

@get('/odjava_uporabnik')
def odjava_uporabnik():
    response.delete_cookie("uporabnik")
    response.delete_cookie("rola")
    return template('prijava_uporabnik.html', napaka=None)






























if __name__ == "__main__":
    run(host='localhost', port=SERVER_PORT, reloader=RELOADER)