def create_cipher_table():
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

cipher_table = create_cipher_table()
text_to_encrypt = "Ich vertraue darauf, dass Gott bei mir bleibt – auch wenn es schwer ist."
encrypted_text = encrypt(text_to_encrypt, cipher_table)

print(f"Original Text: {text_to_encrypt}")
print(f"Cipher text: {encrypted_text}")
