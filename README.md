# ÉNONCÉ EXAMEN FINAL

## Calculatrice en POO avec modules et package

Durée : 2 heures
Modalités :

- Caméra obligatoire pendant toute la durée de l’examen
- Travail individuel
- Aucun partage de code
- Aucun outil d’assistance automatisé
- Tout soupçon de plagiat induira un zéro.

---

# Objectif

Vous devez transformer une calculatrice en une application Python structurée utilisant :

- la programmation orientée objet (POO)
- des modules Python
- un package Python

L’objectif est de démontrer votre capacité à :

- structurer un projet
- créer et utiliser des classes
- séparer les responsabilités
- organiser correctement les imports

---

# Fonctionnalités obligatoires

Votre application doit permettre :

## 1. Opérations à deux nombres

- addition
- soustraction
- multiplication
- division

## 2. Système de mémoires

- mémoires M1 à M5
- stocker un résultat dans une mémoire
- lire une mémoire
- effacer une mémoire
- effacer toutes les mémoires

## 3. Gestion du dernier résultat

- après chaque opération, le résultat doit être conservé
- il doit être possible d’afficher le dernier résultat

---

# Structure obligatoire

Vous devez utiliser exactement cette structure :

```
calculatrice/
├── main.py
└── calculator/
    ├── __init__.py
    ├── engine.py
    ├── memory.py
    ├── ui_console.py
    └── app.py
```

---

# Contraintes techniques

| Module        | input() autorisé | print() autorisé |
| ------------- | ---------------- | ---------------- |
| engine.py     | Non              | Non              |
| memory.py     | Non              | Non              |
| ui_console.py | Oui              | Oui              |
| app.py        | Oui              | Oui              |
| main.py       | Non              | Non              |

Toute violation de cette règle peut entraîner une pénalité.

---

# Carcasse fournie

Vous devez compléter les fichiers suivants.

---

## calculator/**init**.py

```python
# package calculator
```

---

## calculator/engine.py

```python
class CalculatorEngine:

    def add(self, a, b):
        pass

    def sub(self, a, b):
        pass

    def mul(self, a, b):
        pass

    def div(self, a, b):
        pass
```

---

## calculator/memory.py

```python
class MemoryBank:

    def __init__(self):
        self.memories = {
            "M1": None,
            "M2": None,
            "M3": None,
            "M4": None,
            "M5": None
        }

    def store(self, name, value):
        pass

    def read(self, name):
        pass

    def clear(self, name):
        pass

    def clear_all(self):
        pass

    def list_all(self):
        pass
```

---

## calculator/ui_console.py

```python
class ConsoleUI:

    def show_menu(self):
        pass

    def ask_choice(self):
        pass

    def ask_number(self):
        pass

    def ask_operator(self):
        pass

    def show_result(self, result):
        pass

    def show_memories(self, memories):
        pass
```

---

## calculator/app.py

```python
from .engine import CalculatorEngine
from .memory import MemoryBank
from .ui_console import ConsoleUI


class CalculatorApp:

    def __init__(self):
        self.engine = CalculatorEngine()
        self.memory = MemoryBank()
        self.ui = ConsoleUI()
        self.last_result = None

    def run(self):
        pass

    def handle_two_numbers(self):
        pass

    def handle_memory_menu(self):
        pass
```

---

## main.py

```python
from calculator.app import CalculatorApp

def main():
    app = CalculatorApp()
    app.run()

if __name__ == "__main__":
    main()
```

---

# Résultat attendu

L’application doit fonctionner avec :

```
python main.py
```

---

# Bonus (facultatifs)

Les bonus suivants peuvent être réalisés en plus des fonctionnalités obligatoires.

## Bonus 1 — Gestion propre de la division par zéro

- Lever une exception dans `engine.py`
- Gérer cette erreur proprement dans `app.py`
- Afficher un message clair à l’utilisateur

## Bonus 2 — Utilisation du dernier résultat

Permettre à l’utilisateur d’utiliser le dernier résultat comme premier nombre d’une nouvelle opération (exemple : taper `R` pour réutiliser le résultat précédent).

---

L’évaluation portera sur :

- le respect de la structure demandée
- la séparation des responsabilités
- le bon fonctionnement de l’application
- la clarté du code
