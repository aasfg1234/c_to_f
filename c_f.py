#攝氏('C) 轉換成華視('F)程式

#讓使用者輸入 攝氏溫度
#然後印出華氏溫度

temperature_c = input('請輸入攝氏溫度: ')
temperature_c = float(temperature_c)
temperature_f = temperature_c * 9 / 5 + 32
print('華氏溫度為: ', temperature_f)