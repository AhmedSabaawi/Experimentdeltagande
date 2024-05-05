def caesar_encrypt(text, shift):
    encrypted_text = []
    for char in text:
        if char.isupper():
            # Skiftar en stor bokstav
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text.append(new_char)
        elif char.islower():
            # Skiftar en liten bokstav
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text.append(new_char)
        else:
            # Om tecknet inte är en bokstav, lägg till som det är
            encrypted_text.append(char)
    return ''.join(encrypted_text)

# Testa funktionen genom att låta användaren mata in data
if __name__ == "__main__":
    try:
        # Ta emot text och skiftnyckel från användaren
        text = input("Ange text för kryptering: ")
        shift = int(input("Ange skiftnyckel (heltal): "))
        
        # Anropa funktionen och visa den krypterade texten
        encrypted_text = caesar_encrypt(text, shift)
        print(f"Krypterad text: {encrypted_text}")
    except ValueError:
        print("Felaktig inmatning. Vänligen ange ett giltigt heltal för skiftnyckeln.")
