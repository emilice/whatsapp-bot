import pywhatkit as kit
import time

try:
    kit.sendwhatmsg("+905070296933", "Merhaba ben Emine", 18, 16, True , 2 )
    print("Gönderme başarılı.")
except:
    print("Beklenmeyen bir hata oluştu.")
    time.sleep(5)
