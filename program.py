pris = float(input('Vad är grundpriset?'))
ålder = int(input('Vad är åldern?'))
if ålder < 12:
    pris = pris * 2
elif ålder >= 65:
    pris = pris * 0.75
elif ålder >= 100:
    pris = pris * 0,80
else:
    pris = pris * 0.9
print(f'Pris: {pris:.2f} balubas')