""" Módulo de lectura de la instancia """

class leerInstancia():
  n = 0 # cantidad de tiendas
  largos = [] # largo de cada tienda
  matriz = [] # matriz de flujo entre tiendas

  def __init__(self,ruta:str):
    print(f"Leyendo archivo {ruta} ...")
    archivo = open(ruta, "r")
    
    # primera linea, cantidad de tiendas
    linea = archivo.readline()
    self.n = int(linea)
    
    # segunda linea, tamaños de las tiendas
    linea = archivo.readline()
    self.largos = linea.split(sep = ',')
    # pasar a int
    for i in range(self.n):
      self.largos[i] = int(self.largos[i])
    
    # el resto de las lineas corresponden a la matriz
    for i in range(self.n):
      linea = archivo.readline()
      self.matriz.append(linea.split(sep = ','))
    # pasar a int
    for i in range(self.n):
      for j in range(self.n):
        self.matriz[i][j] = int(self.matriz[i][j])
    
  def mostrarInstancia(self):
    print(f"Cantidad de tiendas: {self.n}\n")
    #print(f"Tamaños: {self.largos}\n")
    print("Tamaños tiendas:")
    for i in range(0,len(self.largos)):
      print(f"{i+1}: {self.largos[i]}")
    print("Matriz de flujo entre tiendas:")
    for i in range(self.n):
      print(self.matriz[i])
