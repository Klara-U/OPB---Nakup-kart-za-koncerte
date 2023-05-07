CREATE table Uporabnik(
    username VARCHAR PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email VARCHAR NOT NULL,
    gender TEXT NOT NULL,
    password VARCHAR NOT NULL
);

CREATE table Turneja(
    id_turneja INTEGER PRIMARY KEY,
    id_album VARCHAR REFERENCES Album(id_album)
);

CREATE table Koncert(
    id_koncert INTEGER PRIMARY KEY,
    id_turneja INTEGER REFERENCES Turneja(id_turneja),
    kraj TEXT NOT NULL,
    drzava TEXT NOT NULL,
    datum DATE,
    cena_karte NUMERIC NOT NULL
);

CREATE table Ocena(
    id_ocene INTEGER PRIMARY KEY,
    id_uporabnika VARCHAR REFERENCES Uporabnik(username),
    id_album VARCHAR REFERENCES Album(id_album),
    ocena INTEGER NOT NULL,
    cas DATETIME
);

CREATE table Rezervacija(
    id_rezervacije INTEGER PRIMARY KEY,
    id_uporabnika VARCHAR REFERENCES Uporabnik(username),
    id_koncert INTEGER REFERENCES Koncert(id_koncert),
    cas_rezervacije DATETIME,
    stevilo_kart INTEGER NOT NULL
);

