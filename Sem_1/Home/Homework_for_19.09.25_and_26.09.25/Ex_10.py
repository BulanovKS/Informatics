A = ['а','е', 'ё','и','о','у','ы','э','ю','я']
with open("input_for_10.txt", 'r', encoding="utf_8") as file:
    text = file.read()
    print(text)
with open("input_for_10.txt", 'a', encoding='utf-8') as file:
    file.write('\n')
    file.write(text[0])
    if text[0] in A: file.write('с' + text[0])
    for i in range(1, len(text)):
        file.write(text[i])
        if (text[i] in A) and (text[i - 1] in A): continue
        elif (text[i] in A) and (text[i-1] not in A): file.write('с' + text[i])