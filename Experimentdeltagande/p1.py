def talfoeljd(n):
    return list(range(2, n + 1, 2))

# Testa funktionen genom att låta användaren mata in data
if __name__ == "__main__":
    try:
        # Fråga användaren om ett heltal
        tal = int(input("Ange ett heltal: "))
        
        # Anropa funktionen med användarens indata och skriv ut resultatet
        resultat = talfoeljd(tal)
        print(f"talfoeljd({tal}) returnerar: {resultat}")
    except ValueError:
        print("Felaktig inmatning. Vänligen ange ett giltigt heltal.")
