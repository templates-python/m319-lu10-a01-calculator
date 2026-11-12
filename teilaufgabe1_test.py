"""Unit tests for the exercise (teilaufgabe1)."""


import importlib.util
import os

# Pfad zur Datei teilaufgabe1.py
FILE_PATH = 'teilaufgabe1.py'


def test_import_statement():
    """ Überprüft, ob das Import-Statement für 'calc' vorhanden ist. """
    with open(FILE_PATH, 'r') as file:
        contents = file.read()
        assert 'import calc' in contents, \
            "Import-Statement für 'calc' fehlt."


# Ermitteln des aktuellen Verzeichnispfades
current_directory = os.path.dirname(os.path.abspath(__file__))
# Pfad zum calc-Modul
calc_path = os.path.join(current_directory, 'calc.py')

def test_calc_functions():
    """ Überprüft, ob das Modul 'calc' die Funktionen 'add' und 'mul' enthält. """
    spec = importlib.util.spec_from_file_location('calc', calc_path)
    calc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(calc)

    assert hasattr(calc, 'add'), "Funktion 'add' fehlt in 'calc'."
    assert hasattr(calc, 'mul'), "Funktion 'mul' fehlt in 'calc'."
