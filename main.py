
from pyscript import display, document

non_metals = {
    "H": ("H", "Hydrogen", 1, 1.008),
    "C": ("C", "Carbon", 6, 12.011),
    "N": ("N", "Nitrogen", 7, 14.007),
    "O": ("O", "Oxygen", 8, 15.999),
    "P": ("P", "Phosphorus", 15, 30.974),
    "S": ("S", "Sulfur", 16, 32.06),
    "SE": ("Se", "Selenium", 34, 78.971),
    "F": ("F", "Fluorine", 9, 18.998),
    "CL": ("Cl", "Chlorine", 17, 35.45),
    "BR": ("Br", "Bromine", 35, 79.904),
    "I": ("I", "Iodine", 53, 126.90),
    "HE": ("He", "Helium", 2, 4.0026),
    "NE": ("Ne", "Neon", 10, 20.180),
    "AR": ("Ar", "Argon", 18, 39.948),
    "KR": ("Kr", "Krypton", 36, 83.798),
    "XE": ("Xe", "Xenon", 54, 131.293),
    "RN": ("Rn", "Radon", 86, 222)
}


def search_element(e):
    document.getElementById('result').innerHTML = ""

    element1 = document.getElementById('element_symbol').value.strip().upper()

    symbol, element, atomic_number, atomic_mass = non_metals.get(
        element1, ("-", "Element not found", "-", "-")
    )

    document.getElementById('result').innerHTML = f"""
    <b>Symbol:</b> {symbol} <br>
    <b>Element:</b> {element} <br>
    <b>Atomic Number:</b> {atomic_number} <br>
    <b>Atomic Mass:</b> {atomic_mass}
    """
