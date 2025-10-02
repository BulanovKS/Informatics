with open("input_for_9.txt", 'r') as file:
    text = file.read()
    s = text.count('.') - 2 * text.count('...') + text.count('!') + text.count('?') - text.count('!?')
print(s)