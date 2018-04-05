import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m' 

# Iniciamos los parámetros del script
remitente = 'pruebasinternetiot@gmail.com'
print(bcolors.OKBLUE,'Remitente: <',remitente,'>')
destinatarios = ['pruebasinternetiot@gmail.com']
print('Destinatario: <',destinatarios,'>')
asunto = '[RPI] Tenemos Visita'
print(asunto)
cuerpo = 'Este es el contenido del mensaje'
ruta_adjunto = 'image.jpg'
nombre_adjunto = 'image.jpg'

# Creamos el objeto mensaje
mensaje = MIMEMultipart()
 
# Establecemos los atributos del mensaje
mensaje['From'] = remitente
mensaje['To'] = ", ".join(destinatarios)
mensaje['Subject'] = asunto

# Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
mensaje.attach(MIMEText(cuerpo, 'plain'))
 
# Abrimos el archivo que vamos a adjuntar
archivo_adjunto = open(ruta_adjunto, 'rb')
 
# Creamos un objeto MIME base
adjunto_MIME = MIMEBase('application', 'octet-stream')
# Y le cargamos el archivo adjunto
adjunto_MIME.set_payload((archivo_adjunto).read())
# Codificamos el objeto en BASE64
encoders.encode_base64(adjunto_MIME)
# Agregamos una cabecera al objeto
adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
# Y finalmente lo agregamos al mensaje
mensaje.attach(adjunto_MIME)
 
# Creamos la conexión con el servidor
sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
# Ciframos la conexión
sesion_smtp.starttls()
# Iniciamos sesión en el servidor
sesion_smtp.login('pruebasinternetiot@gmail.com','pruebasinternetiot1')
# Convertimos el objeto mensaje a texto
texto = mensaje.as_string()
# Enviamos el mensaje
sesion_smtp.sendmail(remitente, destinatarios, texto)
# Cerramos la conexión
sesion_smtp.quit()
print('Se ha finalizado el Envio de correo a ...',destinatarios)
print(bcolors.ENDC)
