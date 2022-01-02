from time import strftime, sleep

while True:
	try:
		print(strftime('%H:%M:%S %p'), end="\r", flush=True)
		sleep(1)
	except KeyboardInterrupt:
		break