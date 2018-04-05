import smtplib

fromaddr = 'pruebasinternetiot@gmail.com'
toaddrs  = 'pruebasinternetiot@gmail.com'
msg = 'Correo enviado utilizano Python + smtplib en www.pythondiario.com'
# Datos
username = 'pruebasinternetiot@gmail.com'
password = 'pruebasinternetiot1'
# Enviando el correo
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
