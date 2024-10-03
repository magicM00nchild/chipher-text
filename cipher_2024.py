def create_cipher_table():
    # Erstellen der Chiffriertabelle mit Emojis
    cipher_table = {
        'A': '🥇',
        'B': '🚀',
        'C': '🌙',
        'D': '🍀',
        'E': '🌞',
        'F': '⭐',
        'G': '🍕',
        'H': '🔑',
        'I': '🕒',
        'J': '🎈',
        'K': '🔨',
        'L': '🍉',
        'M': '🎵',
        'N': '📚',
        'O': '🍩',
        'P': '🏆',
        'Q': '💎',
        'R': '🐍',
        'S': '🎯',
        'T': '🔔',
        'U': '✈️',
        'V': '⚡',
        'W': '🍎',
        'X': '🎮',
        'Y': '🧩',
        'Z': '🎻',
        'Ü': '☂',
        'Ö': '☁',
        ' ': ' '  
    }
    return cipher_table

def encrypt(text, cipher_table):
    encrypted_text = ''
    for char in text.upper():  
        encrypted_text += cipher_table.get(char, char)  
    return encrypted_text

# Beispielnutzung
cipher_table = create_cipher_table()
text_to_encrypt = "HELLO WORLD"
encrypted_text = encrypt(text_to_encrypt, cipher_table)

print(f"Ursprünglicher Text: {text_to_encrypt}")
print(f"Verschlüsselter Text: {encrypted_text}")
