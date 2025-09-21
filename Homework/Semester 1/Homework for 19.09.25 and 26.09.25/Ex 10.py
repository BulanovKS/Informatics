A = ['а','е', 'ё','и','о','у','ы','э','ю','я']
with open("input for 10.txt", 'r') as file:
    text = file.read()
    print(text)
with open("input for 10.txt", 'a') as file:
    #file.write('\n')
    for i in range(1, len(text)):
        #file.write(text[i])
        if (text[i] in A) and (text[i-1] not in A): file.write('с' + text[i])