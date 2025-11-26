def replace_letters_with_underscores(text):
    result = ''
    for char in text:
        if char.isalpha():  
            result += '_'  
        else:
            result += char  
    return result

text_to_modify = "Ich vertraue darauf, dass Gott bei mir bleibt – auch wenn es schwer ist"
modified_text = replace_letters_with_underscores(text_to_modify)

print(f"Original Text: {text_to_modify}")
print(f"Modified Text: {modified_text}")
