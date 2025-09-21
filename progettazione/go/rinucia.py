from custom_types import *
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from partita import Partita


class PartitaConRinuncia(Partita):
    _rinunciatario: Rinuncia # <<immutable>> noto alla nascita

    def __init__(self, data: date, indirizzo: Indirizzo, komi: Komi, rinunciatario: Rinuncia):
        super().__init__(data, indirizzo, komi)
        self._rinunciatario = rinunciatario
    
    def getRinunciatario(self):
        return self._rinunciatario
    
    def __str__(self):
        return super().__str__() + f"\nrinucniatario: {self._rinunciatario}"