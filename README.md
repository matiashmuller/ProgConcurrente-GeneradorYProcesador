# Programación Concurrente - UNAHUR

## Ejercicio en Python y Java

Implemente un programa que ejecute 2 hilos llamados procesador y un hilo llamado generador y accediendo todos a una variable global común dato



### Procesador:
Cada hilo procesador debe tomar el valor de la variable dato y generar un mensaje con su valor (por ejemplo: Se proceso el dato : 58). 
Esto lo debe hacer en un loop infinito con un retardo aleatorio entre 1 y 5 segundos entre iteraciones.
Ejemplo del loop Procesador (operación básica, no incluye el código necesario para funcionar tal como lo piden los requerimientos):

```
while True:
    logging.info(f'Se proceso el dato : {datos}')

    if leido == False:

        leido = True

    time.sleep(random.randint(1,5))
```

Nota: "leido" es una variable global de tipo bool que indica si algún hilo procesador leyó la variable datos luego que fue actualizada con un valor nuevo: False ningún hilo leyó la variable, True: al menos un hilo leyó la variable.

Nota: El uso de este ejemplo en la solución es opcional, puede modificarlo o incluso utilizar uno completamente diferente si lo consideran necesario.


### Generador:
El hilo generador, debe cargar en forma continua (loop) un valor entero aleatorio entre 0 y 100 en la variable global dato y generar un mensaje con el valor asignado, (por ejemplo: Se generó un nuevo dato = 63). 
Luego de asignar el nuevo valor a dato, el generador debe verificar que por lo menos un procesador lo haya leído antes de continuar con la siguiente iteración.
No importa la cantidad de procesadores que lean datos, lo importante es que todos los datos generados por el generador sean leídos por al menos un procesador. 

Ejemplo del loop Procesador (operación básica, no incluye el código necesario para funcionar tal como lo piden los requerimientos):

```
while True:

    datos = random.randint(0,100)

    logging.info(f'Se generó un nuevo dato = {datos}')

    leido = False
```

Nota: leido es una variable global de tipo bool que indica si algún hilo procesador leyó la variable datos luego que fue actualizada con un valor nuevo: False ningún hilo leyó la variable, True: al menos un hilo leyó la variable.

Nota: El uso de este ejemplo en la solución es opcional, puede modificarlo o incluso utilizar uno completamente diferente si lo consideran necesario.


El programa debe funcionar para cualquier número de procesadores.
Debe colocarse el código suficiente para evitar condiciones de carrera.

Ejemplo de salida:

```
20:10:31.327 [Thread-1] - Se generó un nuevo dato = 48

20:10:31.327 [Thread-2] - Se proceso el dato : 48

20:10:31.328 [Thread-1] - Se generó un nuevo dato = 58

20:10:31.328 [Thread-3] - Se proceso el dato : 58

20:10:31.328 [Thread-4] - Se procesó el dato : 58

20:10:31.328 [Thread-1] - Se generó un nuevo dato = 63

20:10:31.328 [Thread-5] - Se proceso el dato : 63

20:10:31.328 [Thread-1] - Se generó un nuevo dato = 86

20:10:32.332 [Thread-3] - Se proceso el dato : 86

20:10:32.332 [Thread-1] - Se generó un nuevo dato = 90

20:10:34.336 [Thread-3] - Se proceso el dato : 90

```