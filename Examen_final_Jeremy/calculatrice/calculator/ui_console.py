class ConsoleUI:
    def show_menu(self):
        print("\n=== CALCULATRICE (POO) ===")
        print("1. Opérations à deux nombres")
        print("2. Système de mémoires (M1 à M5)")
        print("3. Afficher le dernier résultat")
        print("0. Quitter")

    def ask_choice(self):
        while True:
            choice = input("Votre choix : ").strip()
            if choice in {"0", "1", "2", "3"}:
                return int(choice)
            print("Choix invalide. Recommence.")

    def ask_operator(self):
        while True:
            op = input("Choisissez l'opérateur (+, -, *, /) : ").strip()
            if op in {"+", "-", "*", "/"}:
                return op
            print("Opérateur invalide.")

    def ask_number(self, prompt, allow_last=False, last_result=None):
        while True:
            txt = input(prompt).strip()

            # Bonus: R pour réutiliser le dernier résultat
            if allow_last and txt.upper() == "R":
                if last_result is None:
                    print("Aucun dernier résultat disponible.")
                    continue
                return last_result

            try:
                return float(txt)
            except ValueError:
                print("Veuillez entrer un nombre valide (ex: 12, 3.5)")

    def show_result(self, result):
        print(f"Résultat : {result}")

    def show_message(self, msg):
        print(msg)

    def show_memories(self, memories_dict):
        print("\n--- Mémoires ---")
        for k, v in memories_dict.items():
            print(f"{k} = {v}")
