## INF3144 - Tarea 2: Metaheurísticas

INTEGRANTES:
- Katherine Sepúlveda (20.479.664-5)
- Joaquin Llanten (21.086.600-0)
- Francesco Riffo (19.613.343-7)

# INSTRUCCIONES

Para ejecutar el código dentro de Replit, introducir en la Shell el comando "python3 main.py". Si se prueba en otro entorno, basta con ejecutar el archivo main.py.

En caso de querer ejectuar otras instancias, manipular el archivo main.py cambiando la ruta de lectura de la instancia, ubicada en la linea 6 del archivo.

Con este [link](https://repl.it/github/kathe00/INF3144_Tarea2), puede importar el proyecto a la plataforma Repl.it.

## Cambio de instancia
- Cambiar ejecución de QAP_sko56_04_n.txt a QAP_sko100_04_n.txt
\
instancia = leerInstancia("./Instancias/ (instancia a ejecutar) ")
\
instancia = leerInstancia("./Instancias/QAP_sko56_04_n.txt")
\
instancia = leerInstancia("./Instancias/QAP_sko100_04_n.txt")


Para ingresar a otras instancias, acceder a las carpetas mediante un slash "/", seleccionando el archivo al último, junto con su extensión en .txt

- Ingresar a instancias adicionales
\
instancia = leerInstancia("./Instancias/ (carpeta) / (archivo)")
\
instancia = leerInstancia("./Instancias/instancias_extra/instancias_adicionales/SRFLP_Rubio_AnKeVa_500_03.txt")

Si está trabajando de manera local, recuerde siempre guardar los cambios antes de ejecutar el programa para ver sus cambios reflejados en los resultados.

## Cambio de parámetros
El cambio de parámetros, se realiza de manera manual a gusto del usuario.

Para realizar cambio de parámetros, partimos por entrar al archivo "SA.py", que es el módulo que contiene la metaheuristica de Simulated Annealing. 

Dentro de la primera función, "__ init __", se encuentran los parámetros que utiliza el algoritmo. Para cambiarlos basta con modificar cualquiera de los valores, bajo su propio criterio.
