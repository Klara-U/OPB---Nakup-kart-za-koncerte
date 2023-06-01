from Database import Repo
from Modeli import *
from typing import Dict
from re import sub
import dataclasses
import bcrypt
from typing import Type
from datetime import date

class AuthService:

    repo : Repo
    def __init__(self, repo : Repo):
        self.repo = repo

    def obstaja_uporabnik(self, uporabnik:str) -> bool:
        try:
            user = self.repo.dobi_gen_id(Uporabnik, uporabnik, )
