import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sp

#Чтение файла
rate, aud_data = sp.wavfile.read("Kukushka_cut.wav")
len_data = len(aud_data)
n = 2**(int(np.ceil(np.log2(len_data))))
channel_1 = np.zeros(n)
channel_1[0:len_data] = aud_data

#Проведение FFT
fourier = np.fft.rfft(channel_1)
frequencies = np.fft.rfftfreq(2*len(fourier)-1, d=1/rate)

#Визуализация до
plt.figure(figsize=(10, 4))
plt.plot(frequencies, np.abs(fourier), color="red", alpha=0.5, label="Cпектр до обработки")

#Вырезание частот
# clip = [(15000, "")] #не сказывается на качестве звука
# clip = [(0, 500), (15000, "")] # звук стал чище (убраны низкие частоты)
clip = [(0, 500), (3000, 5000), (15000, "")] # (x_left, x_right) набор вырезаемых частот
k = n/rate
for clip in clip:
    if len(clip) == 0: break
    if clip[1] == "":
        fourier[int(clip[0]*k):] = np.zeros(len(fourier) - int(clip[0]*k))
    elif clip[0] == "":
        fourier[:int(clip[1]*k)] = np.zeros(len(fourier) - int(clip[1]*k))
    else:
        fourier[int(clip[0]*k):int(clip[1]*k)] = np.zeros(int(clip[1]*k) - int(clip[0]*k))

#Изменение амплитуды
# volume = [(500, 2000, 1.5)]
volume = [(500, 2000, 3)] # (x_left, x_right, t) набор частот и изменение амплитуды в t раз
k = n/rate
for v in volume:
    if len(volume) == 0: break
    if v[1] == "":
        fourier[int(v[0]*k):] = v[2] * fourier[int(v[0]*k):]
    elif v[0] == "":
        fourier[:int(v[1]*k)] = v[2] * fourier[:int(v[1]*k)]
    else:
        fourier[int(v[0]*k):int(v[1]*k)] = v[2] * fourier[int(v[0]*k):int(v[1]*k)]

#Проведение ОБПФ
output = np.fft.irfft(fourier)
output_t = output.astype(np.float32)

sp.wavfile.write("output.wav", rate, output_t[:len_data])

#Визуализация после
plt.plot(frequencies, -np.abs(fourier), color="blue", alpha=0.5, label="Cпектр после обработки \n (Отражен вниз)")
plt.title('Частотный спектр (песня В. Цоя "Кукушка")')
plt.xlabel("Частота (Гц)")
plt.ylabel("Амплитуда")
plt.grid(True)
plt.legend()
plt.show()
