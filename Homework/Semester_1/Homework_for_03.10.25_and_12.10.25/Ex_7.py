import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

with open("input_for_7.txt", 'r', encoding="utf_8") as file:
    text = file.read()
    #дописать разбиение текста на слова (замена всех знаков пунктуации на пробелы), привести все строки к нижнему виду
    words = {word: amount for word, amount in zip([text[i] for i in range(len(text))], [0] * len(text))}
    for i in range(len(text)):
        if text[i] in words:
            words[text[i]] += 1
    print(text)