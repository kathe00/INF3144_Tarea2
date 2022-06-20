import math
import random

class SimualtedAnnealing():
  
  def __init__(self):
    # parámetros
    self.temp = 1000000 # temperatura
    self.temp_min = 0.000001 # temperatura   minima
    self.alpha = 0.98 # alpha
    self.vecindario = 30 # tamaño del vecindario en el que se buscará

   
  def solucionInicial(self, instancia):
    # Selección Aleatoria Uniforme
    # 1. Tomar el orden incial:
    lista = list(range(1,instancia.n+1)) # se crea una lista con los nros del 1 a n
    print(f"Lista inicial: {lista}")
    solucion = [] # y una lista vacia para la solución

    # 2. Aplicar el algoritmo:
    while lista:
      # tomar una posición aleatoria (de 0 al largo de la lista)
      rand = random.randint(0, len(lista) - 1)
      
      # agregar el elemento a la solucion
      solucion.append(lista[rand])
      
      # quitar el elemento
      lista.pop(rand)

    # 3. Retornar la solución
    return solucion
    

  def criterioTermino(self, temperatura):
    # Verificamos que la temperatura no este inicializada en 0, lo que permite que no se genere un bucle infinito.
    if (self.temp_min > 0):
      # mientras la temperatura sea mayor al minimo, continuar
      if (temperatura >= self.temp_min):
        return True
    return False

  
  def siguienteVecino(self, solucion):
    sol = solucion.copy()
    
    # SWAP
    # 1. Elejir 2 posiciones randoms de la solución
    pos1 = random.randint(0, len(sol) - 1)
    pos2 = random.randint(0, len(sol) - 1)

    # verificar que no sean iguales
    while pos1 == pos2:
      pos2 = random.randint(0, len(sol) - 1)

    # 2. Hacemos el intercambio con ayuda de un auxiliar
    # guardamos el valor ubicado en la posición 1
    aux = sol[pos1]
    # cambiamos el valor de la posición 1 por la 2
    sol[pos1] = sol[pos2]
    # cambiamos el valor de la posicion 2 por el que estaba en la 1
    sol[pos2] = aux

    # 3. Retornamos la solución encontrada
    return sol

  # buscar uno de los mejores vecinos
  def siguienteMejorVecino(self, solucion, instancia):
    
    mejor = self.siguienteVecino(solucion)
    sol = solucion.copy()

    # listas de posiciones a intercambiar
    pos1 = random.sample(range(instancia.n-1), self.vecindario)
    pos2 = random.sample(range(instancia.n-1), self.vecindario)

    # comprobar que no se trate de intercambiar la misma posicion
    for i in range(len(pos1)):
      if pos1[i] == pos2[i]:
        pos2[i] = pos2[i]+1
        # faltaría comprobar que la nueva pos2 no se haya usado antes con la misma pos1
        
    for i in range(self.vecindario): #se buscara entre n vecinos al hazar
      # SWAP
      # 1. Tomamos las 2 posiciones del indice i
      # 2. Hacemos el intercambio con ayuda de un auxiliar
      # guardamos el valor ubicado en la posición 1
      aux = sol[pos1[i]]
      # cambiamos el valor de la posición 1 por la 2
      sol[pos1[i]] = sol[pos2[i]]
      # cambiamos el valor de la posicion 2 por el que estaba en la 1
      sol[pos2[i]] = aux

      # 3. Comprobamos si es mejor que la anterior
      if (self.funcionObjetivo(mejor, instancia) > self.funcionObjetivo(sol, instancia)):
        mejor = sol.copy()

    # 4. Retornamos la solución encontrada
    return mejor

    
  def criterioAceptacion(self, actual, siguiente, temperatura):
    # Se aplica Criterio de Metrópolis
    delta = siguiente - actual
    #print(f"delta = {delta}")

    if delta < 0:
      # si el delta es negativo, la solución siguiente es mejor y se acepta automáticamente.
      print("Es mejor, se acepta.")
      return True 
      
    if temperatura == 0:
      # esto creo que ni debería pasar si la temp minima es 0.2
      print("la vaina de la temperatura acaba de pasar")
      return False

    # probabilidad de aceptación si la solucion siguiente es peor
    div = (delta * -1) / temperatura
    prob = math.exp(div)
    nro = random.random()
    print(f"prob = {prob}")
    print(f"nro = {nro}")

    # se acepta según la probabilidad
    if ( nro < prob):
      print("Se acepta por probabilidad.")
      return True
    else:
      print("No se acepta.")
    
    return False

  
  def funcionObjetivo(self, solucion, instancia):
    # La función objetivo calcula el esfuerzo que deben aplicar los clientes

    # Cálculo de la Función Objetivo
    # 1. Por cada sumatoria se realiza un ciclo for
    # el esfuerzo comienza en 0
    esfuerzo = 0
    for i in range(0, len(solucion)-1):
      for j in range (i+1, len(solucion)):
        # 2. Se calcula la distancia entre los puestos i y j (función d(i,j))
        # se utiliza la mitad del primer puesto
        distancia = instancia.largos[solucion[i]-1] / 2
        # más los largos de los intermedios
        # (pero si j está justo al lado de i, no hay puestos intermedios)
        if j != i+1:
          for k in range(i+1,j):
            distancia += instancia.largos[solucion[k]-1]
        # más la mitad del último
        distancia += instancia.largos[solucion[j]-1] / 2

        # 3. Y se multiplica por el flujo entre los puestos i y j
        esfuerzo += distancia * instancia.matriz[solucion[i]-1][solucion[j]-1]
    
    # 4. Y retornamos el esfuerzo total calculado
    return esfuerzo
    

  def buscar(self, instancia):
    # obtener la solución y parámetros iniciales
    solucion = self.solucionInicial(instancia)
    mejor_solucion = solucion.copy()
    temperatura = self.temp
    iteraciones = 0

    print("Solución inicial:")
    print(solucion)
    print(f"largo solucion inicial: {len(solucion)}")
    #print(len(solucion))
    print(f"Función Objetivo: {self.funcionObjetivo(solucion, instancia)}\n")

    # mientras se cumpla el criterio de término, se sigue iterando
    while self.criterioTermino(temperatura):
      # tomamos un vecino de la actual solucion
      #solucion_sig = self.siguienteVecino(solucion)
      solucion_sig = self.siguienteMejorVecino(solucion, instancia)
      iteraciones += 1

      # calculamos las funciones objetivo de la solucion anterior (o actual) y la siguiente
      fObj = self.funcionObjetivo(solucion, instancia)
      fObj_sig = self.funcionObjetivo(solucion_sig, instancia)

      print(f"Se encontró: {fObj_sig}")

      # evaluamos segun la funcion objetivo y el criterio de aceptación
      if self.criterioAceptacion(fObj, fObj_sig, temperatura):
        solucion = solucion_sig.copy()
        
      # si la solución encontrada es mejor que la actual mejor solución, se cambia
      if self.funcionObjetivo(solucion, instancia) < self.funcionObjetivo(mejor_solucion, instancia):
        print("Nueva mejor solución encontrada.")
        mejor_solucion = solucion.copy()
      # enfriar a temperatura
      temperatura = self.alpha * temperatura
      print(f"T = {temperatura}")
      print()

    # se retorna la mejor solución
    return mejor_solucion, self.funcionObjetivo(mejor_solucion, instancia), iteraciones

  