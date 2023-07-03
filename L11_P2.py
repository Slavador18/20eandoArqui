#!/usr/bin/env python
from socket import AF_INET, SOCK_DGRAM
import datetime
from threading import Thread
import socket
import struct
import time

servidores_ntp = [
	"0.uk.pool.ntp.org",    # Londres(Reino Unido)
	"1.es.pool.ntp.org",    # Madrid (España)
	"0.us.pool.ntp.org",    # Nueva York(Estados Unidos)
	"0.hk.pool.ntp.org",    # Hong Kong
	"0.jp.pool.ntp.org"     # Tokyo(Japón)
]

"""
Función: get_ntp_time
Descripción: Imprime la  fecha-hora actual en un país determinado
Entrada: Cualquiera de las URLs definidas en la lista servidores_ntp
Salida: Retorna la fecha-hora(timestamp) en formato datetime.datetime, también la imprime
IMPORTANTE: NO modifique esta funcion 
"""
def get_ntp_time(host):
	timezone_dict = {'uk': ['UK', 0 * 3600], 'es': ['España', 1 * 3600],
	                 'hk': ['Hong Kong', 8 * 3600], 'jp': ['Japón', 9 * 3600],
	                 'us': ['Estados Unidos', -5*3600]}
	key = ''
	port = 123
	buf = 1024
	address = (host, port)
	msg = b'\x1b' + 47 * b'\0'

	# reference time (in seconds since 1900-01-01 00:00:00)
	TIME1970 = 2208988800  # 1970-01-01 00:00:00
	# connect to server
	client = socket.socket(AF_INET, SOCK_DGRAM)
	client.sendto(msg, address)
	msg, address = client.recvfrom(buf)
	t = struct.unpack("!12I", msg)[10]
	t -= TIME1970
	client.close()

	for each_key in timezone_dict:
		if each_key in host:
			key = each_key
			break
	print(f"Hora en {timezone_dict[key][0]}: {datetime.datetime.utcfromtimestamp(t + timezone_dict[key][1])}")
	return datetime.datetime.utcfromtimestamp(t + timezone_dict[key][1])


def encontrarPais():
	delta_menor = 25
	pais_proximo = '' # País máx próximo a abrir
	i = 0
	for pais in servidores_ntp:
			time_there = get_ntp_time(pais).hour 
			if (time_there > 8):
				delta = 24 - time_there + 8
			else:
				delta = 8 - time_there
			
			if delta < delta_menor:
				delta_menor = delta
				pais_proximo = i
			i += 1 # Contador de paises
	
	print(f"El país con hora más cercana es: {paises[pais_proximo]}")

delta_lst = [0, 0, 0, 0, 0]

def diferenciaTiempo(index):
	global menorDelta
	global pais_proximo

	time_there = get_ntp_time(servidores_ntp[index]).hour 
	if (time_there > 8):
		delta = 24 - time_there + 8
	else:
		delta = 8 - time_there
	
	delta_lst[index] = delta


def encontrarPaisThreads():
	t1 = Thread(target=diferenciaTiempo, args=(0))
	t2 = Thread(target=diferenciaTiempo, args=(1))
	t3 = Thread(target=diferenciaTiempo, args=(2))
	t4 = Thread(target=diferenciaTiempo, args=(3))
	t5 = Thread(target=diferenciaTiempo, args=(4))

	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t5.start()



if __name__ == '__main__':
	paises = ["UK", "España", "Estados Unidos", "Hong Kong", "Japón"]
	tic = time.perf_counter()
	encontrarPais()
	toc = time.perf_counter()
	print(f"Tiempo de ejecución: {toc-tic} segundos")

	tic = time.perf_counter()
	encontrarPaisThreads()
	toc = time.perf_counter()
	print(f"Tiempo de ejecución: {toc-tic} segundos")



