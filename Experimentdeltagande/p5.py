from collections import defaultdict
import string

def bokstavsfrekvens(text):
    # Skapa en ordbok för att lagra bokstävernas frekvens
    frequency = defaultdict(int)
    
    # Gå igenom varje tecken i texten
    for char in text:
        # Kontrollera om tecknet är en bokstav (ignorera specialtecken och siffror)
        if char.isalpha():
            frequency[char] += 1
    
    return dict(frequency)

# Testa funktionen genom att låta användaren mata in data
if __name__ == "__main__":
    text = input("Ange en textsträng för att analysera bokstavsfrekvens: ")
    
    # Anropa funktionen och visa resultatet
    resultat = bokstavsfrekvens(text)
    print(f"Bokstavsfrekvens: {resultat}")
