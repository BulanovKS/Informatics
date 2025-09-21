with open("input for 9.txt", 'r') as file:
    text = file.read()
    s = text.count('.') - 2 * text.count('...') + text.count('!') + text.count('?') - text.count('!?')
print(s)