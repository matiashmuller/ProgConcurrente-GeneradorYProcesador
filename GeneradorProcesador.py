import logging
import random
import threading
import time

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

dato = None
lock = threading.Lock()
leido = True

class Generador(threading.Thread):
    def __init__(self):
        super().__init__()
        
    def run(self):
        while True:
            with lock:
                global leido
                if leido:
                    global dato
                    dato = random.randint(0,100)
                    logging.info(f"El {threading.current_thread().name} generó el dato: "+str(dato))
                    leido = False

class Procesador(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            with lock:
                global leido
                if not leido:
                    global dato
                    logging.info(f"El {threading.current_thread().name} procesó el dato: "+str(dato))
                    leido = True
            time.sleep(random.randint(1,5))

def generarProcesadores(cantidad):
    for i in range(cantidad):
        procesador = Procesador()
        procesador.start()

gen1 = Generador()

def main():
    gen1.start()
    generarProcesadores(2)

main()




