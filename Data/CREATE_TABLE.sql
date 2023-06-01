DROP table if exists Uporabnik CASCADE;
DROP table if exists Turneja CASCADE;
DROP table if exists Koncert CASCADE;
DROP table if exists Ocena CASCADE;
DROP table if exists Rezervacija CASCADE;

SET datestyle = "ISO, MDY";

CREATE table Uporabnik(
    uporabnisko_ime VARCHAR PRIMARY KEY,
    ime TEXT NOT NULL,
    priimek TEXT NOT NULL,
    email VARCHAR NOT NULL,
    spol TEXT NOT NULL,
    geslo VARCHAR NOT NULL
);

CREATE table Turneja(
    id_turneja VARCHAR PRIMARY KEY,
    id_album VARCHAR 
);

CREATE table Koncert(
    id_koncert INTEGER PRIMARY KEY,
    id_turneja VARCHAR REFERENCES Turneja(id_turneja),
    kraj TEXT NOT NULL,
    drzava TEXT NOT NULL,
    datum DATE,
    cena_karte NUMERIC NOT NULL
);

CREATE table Ocena(
    id_ocena INTEGER PRIMARY KEY,
    id_uporabnik VARCHAR REFERENCES Uporabnik(uporabnisko_ime),
    id_album VARCHAR,
    ocena INTEGER NOT NULL,
    cas DATE
);

CREATE table Rezervacija(
    id_rezervacija INTEGER PRIMARY KEY,
    id_uporabnik VARCHAR REFERENCES Uporabnik(uporabnisko_ime),
    id_koncert INTEGER REFERENCES Koncert(id_koncert),
    cas_rezervacije DATE,
    stevilo_kart INTEGER NOT NULL
);

