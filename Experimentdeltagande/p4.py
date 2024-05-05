import re
from collections import defaultdict

def ordfrekvens(text):
    # Använd regular expression för att extrahera ord och ignorera specialtecken
    words = re.findall(r'\b\w+\b', text)
    
    # Skapa en ordbok för att lagra ordens frekvens
    frequency = defaultdict(int)
    
    for word in words:
        frequency[word] += 1
    
    return dict(frequency)

# Testa funktionen genom att låta användaren mata in data
if __name__ == "__main__":
    text = input("Ange en textsträng för att analysera ordfrekvens: ")
    
    # Anropa funktionen och visa resultatet
    resultat = ordfrekvens(text)
    print(f"Ordfrekvens: {resultat}")
