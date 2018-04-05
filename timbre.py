# boton se conecta en 3 y en 8 de la parte externa de los pines
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(24, GPIO.OUT)  #LED to GPIO24

try:
	while True:
		button_state = GPIO.input(23)
		if button_state == False:
			GPIO.output(24, True)
			print("Activando Camara...")
			print("Capturando Imagen")
			os.system("telegram-send 'Alguien toco el timbre'")
			#os.system("cd images/")
			#os.system("raspistill -o image.jpg")
			#print("Foto almacenada en: ",os.getcwd())
			#os.system("cd ..")
			#print("Enviando correo ...")
			#os.system("python3 mailf.py")
			#os.system("python3 main.py")
			time.sleep(0.2)
		else:
			GPIO.output(24, False)
except:
	GPIO.cleanup()
