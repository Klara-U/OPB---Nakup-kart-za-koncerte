from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Uporabnik:
    username: str = field(default="")
    first_name: str = field(default="")
    last_name: str = field(default="")
    email: str = field(default="")
    gender: str = field(default="")
    password: str = field(default="")

    
@dataclass_json
@dataclass
class Turneja:
    id_turneja: int = field(default=0)
    id_album: str = field(default="")

@dataclass_json
@dataclass
class Koncert:
    id_koncert: int = field(default=0)
    id_turneja: int = field(default=0)
    kraj: str = field(default="")
    drzava: str = field(default="")
    datum: str = field(default="")
    cena_karte: float = field(default=0)

@dataclass_json
@dataclass
class Ocena:
    id_ocene: int = field(default=0)
    id_uporabnika: str = field(default="")
    id_album: str = field(default="")
    ocena: int = field(default=0)
    cas: str = field(default="")

@dataclass_json
@dataclass
class Rezervacija:
    id_rezervacije: int = field(default=0)
    id_uporabnika: str = field(default="")
    id_koncert: int = field(default=0)
    cas_rezervacije: str = field(default="")
    stevilo_kart: int = field(default=0)


