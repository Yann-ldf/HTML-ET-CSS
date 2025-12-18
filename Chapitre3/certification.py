"""
Fichier: Chapitre3/certification.py
Classe `Certification` pour stocker des certifications et diplômes.
"""
from typing import List, Optional, Dict

class Certification:
    """Représente les certifications/diplômes d'une personne.

    Attributs:
        cnil (bool): possession de la certification CNIL
        anssi (bool): possession de la certification ANSSI
        pix (Optional[str]): niveau PIX (ex: 'Intermédiaire', 'Niveau 2')
        diplomas (List[str]): liste de diplômes (ex: 'Baccalauréat', 'Brevet')
    """

    def __init__(self, cnil: bool = False, anssi: bool = False,
                 pix: Optional[str] = None, diplomas: Optional[List[str]] = None):
        self.cnil = bool(cnil)
        self.anssi = bool(anssi)
        self.pix = pix
        self.diplomas = list(diplomas) if diplomas else []

    def add_bac(self, mention: Optional[str] = None) -> None:
        """Ajoute le Baccalauréat, optionnellement avec une mention."""
        name = "Baccalauréat"
        if mention:
            name += f" ({mention})"
        if name not in self.diplomas:
            self.diplomas.append(name)

    def add_brevet(self) -> None:
        """Ajoute le Brevet des collèges."""
        name = "Brevet des collèges"
        if name not in self.diplomas:
            self.diplomas.append(name)

    def add_diploma(self, diploma: str) -> None:
        """Ajoute un diplôme générique si non déjà présent."""
        if diploma and diploma not in self.diplomas:
            self.diplomas.append(diploma)

    def remove_diploma(self, diploma: str) -> bool:
        """Supprime un diplôme, retourne True si supprimé."""
        try:
            self.diplomas.remove(diploma)
            return True
        except ValueError:
            return False

    def set_pix(self, level: str) -> None:
        """Définit le niveau PIX."""
        self.pix = level

    def to_dict(self) -> Dict[str, object]:
        """Retourne une représentation dict des certifications."""
        return {
            "cnil": self.cnil,
            "anssi": self.anssi,
            "pix": self.pix,
            "diplomas": list(self.diplomas),
        }

    def __repr__(self) -> str:
        return (f"Certification(cnil={self.cnil}, anssi={self.anssi}, pix={self.pix!r}, 
                diplomas={self.diplomas})")


if __name__ == "__main__":
    # Exemple d'utilisation
    c = Certification(cnil=True, anssi=False)
    c.set_pix("Intermédiaire")
    c.add_bac("Bien")
    c.add_brevet()
    c.add_diploma("Licence 1 informatique")

    print("Objet:", c)
    print("Dictionnaire:", c.to_dict())
