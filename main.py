from leerInstancia import leerInstancia
from SA import SimualtedAnnealing
import time

# Leer la instancia
instancia = leerInstancia("./Instancias/QAP_sko56_04_n.txt")
sa = SimualtedAnnealing()

# Mostrar la instancia
print(f"\n-- Instancia de tamaño {instancia.n} leída --\n")
#instancia.mostrarInstancia()

print("Buscando mejor solución...\n")
# Implementación de la Metaheurística
inicio = time.time()
mejor_solucion, fObj, iter = sa.buscar(instancia = instancia)
fin = time.time()

print("Mejor solucion encontrada: ")
print(mejor_solucion)
print(f"Valor Funcion Objetivo: {fObj}")
#print(f"Largo: {len(mejor_solucion)}")
print(f"Se relizaron {iter} iteraciones.")
print(f"Tiempo de ejecucion: {fin - inicio}") # sin contar lectura de la instancia