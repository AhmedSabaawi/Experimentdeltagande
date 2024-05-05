def primtal(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Testa funktionen genom att låta användaren mata in data
if __name__ == "__main__":
    try:
        # Fråga användaren om ett heltal för primtalskontroll
        tal = int(input("Ange ett heltal för att kontrollera om det är ett primtal: "))
        
        # Anropa funktionen och skriv ut resultatet
        resultat = primtal(tal)
        if resultat:
            print(f"{tal} är ett primtal.")
        else:
            print(f"{tal} är inte ett primtal.")
    except ValueError:
        print("Felaktig inmatning. Vänligen ange ett giltigt heltal.")
