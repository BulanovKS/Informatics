import string
with open("input_for_7.txt", 'r', encoding="utf_8") as file:
    text = file.read()
    text = (text.translate(str.maketrans('', '', string.punctuation))).lower()
    text_list = text.split(" ")
    words = {word: amount for word, amount in zip(text_list, [0] * len(text))}
    if "" in words: del words[""]
    for i in range(len(text_list)):
        if text_list[i] in words:
            words[text_list[i]] += 1
    words_10 = [0] * 10
    for i in range(10):
        max_value = 0
        for key in words:
            if words[key] > max_value:
                max_value = words[key]
                words_10[i] = key
        del words[words_10[i]]
    print(words_10)