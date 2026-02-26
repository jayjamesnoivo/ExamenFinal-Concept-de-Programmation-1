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
        while True:
            self.ui.show_menu()
            choice = self.ui.ask_choice()

            if choice == 0:
                self.ui.show_message("Au revoir!")
                break
            elif choice == 1:
                self.handle_two_numbers()
            elif choice == 2:
                self.handle_memory_menu()
            elif choice == 3:
                self.ui.show_message(f"Dernier résultat : {self.last_result}")

    def handle_two_numbers(self):
        a = self.ui.ask_number(
            "Entrez le premier nombre (ou R pour dernier résultat) : ",
            allow_last=True,
            last_result=self.last_result
        )
        b = self.ui.ask_number("Entrez le deuxième nombre : ")
        op = self.ui.ask_operator()

        try:
            if op == "+":
                result = self.engine.add(a, b)
            elif op == "-":
                result = self.engine.sub(a, b)
            elif op == "*":
                result = self.engine.mul(a, b)
            else:  # "/"
                result = self.engine.div(a, b)

            self.last_result = result
            self.ui.show_result(result)

        except ZeroDivisionError:
            self.ui.show_message("Erreur : division par zéro impossible.")

    def handle_memory_menu(self):
        while True:
            self.ui.show_message("\n=== MÉMOIRES ===")
            self.ui.show_message("1. Afficher toutes les mémoires")
            self.ui.show_message("2. Stocker le dernier résultat dans une mémoire")
            self.ui.show_message("3. Lire une mémoire")
            self.ui.show_message("4. Effacer une mémoire")
            self.ui.show_message("5. Effacer toutes les mémoires")
            self.ui.show_message("0. Retour")

            choice = input("Votre choix : ").strip()

            if choice == "0":
                return

            if choice == "1":
                self.ui.show_memories(self.memory.list_all())

            elif choice == "2":
                if self.last_result is None:
                    self.ui.show_message("Aucun dernier résultat à stocker.")
                    continue
                name = input("Dans quelle mémoire (M1..M5) ? ").strip().upper()
                try:
                    self.memory.store(name, self.last_result)
                    self.ui.show_message(f"{name} <- {self.last_result}")
                except ValueError:
                    self.ui.show_message("Mémoire invalide (utilise M1 à M5).")

            elif choice == "3":
                name = input("Quelle mémoire lire (M1..M5) ? ").strip().upper()
                try:
                    val = self.memory.read(name)
                    self.ui.show_message(f"{name} = {val}")
                except ValueError:
                    self.ui.show_message("Mémoire invalide (utilise M1 à M5).")

            elif choice == "4":
                name = input("Quelle mémoire effacer (M1..M5) ? ").strip().upper()
                try:
                    self.memory.clear(name)
                    self.ui.show_message(f"{name} effacée.")
                except ValueError:
                    self.ui.show_message("Mémoire invalide (utilise M1 à M5).")

            elif choice == "5":
                self.memory.clear_all()
                self.ui.show_message("Toutes les mémoires ont été effacées.")

            else:
                self.ui.show_message("Choix invalide.")
