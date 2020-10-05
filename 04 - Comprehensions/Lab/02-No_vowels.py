text = input()
no_vowels_text = [c for c in text if c.lower() not in 'aouei']
print(''.join(no_vowels_text))