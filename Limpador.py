
def valorAdjacencia(esta_i, esta_j):
    
    vet_map = mapa()
    num_linha = len(vet_map)
    num_coluna = len(vet_map[0])
    for i in range(num_linha):
      for j in range(num_coluna):
        if i == esta_i and j == esta_j:
          mapaAtualizado(i,j)
          v = [vet_map[i][j-1],vet_map[i+1][j+1],vet_map[i][j+1],vet_map[i-1][j]]
    # print('v = ', v)
    # print('Mapa do valorAdjacencia = ', vet_map)
    return v

def direcaoDeIda(esta_i, esta_j):
  vaga = -1
  pode_ir = valorAdjacencia(esta_i, esta_j)
  for i in range(len(pode_ir)):
    if(pode_ir[i] == 0):
      return i

  return vaga

#Cria a matriz que representa o mapa
def mapa():
  #Matriz que representa o mapa  
  mat_map = []
  for i in range(5):
    list.append(mat_map,[0]*5)
  parede(mat_map)
  return mat_map


def mapaAtualizado(j,i):
  map_atualiza[i][j] = 1
  print('Mapa atualizado = ', map_atualiza)

#Cria as paredes do mapa    
def parede(mat_map):
  num_linha = len(mat_map)
  num_coluna = len(mat_map[0])
  for i in range(num_linha):
    for j in range(num_coluna):
      if i == 0 or j == 0 or j == 4 or i == 4:
        mat_map[i][j] = 1
  return mat_map
    
def mover(esta_i, esta_j):
  vet_map = mapa()
  pos_vaga = direcaoDeIda(esta_i, esta_j)
  if pos_vaga == 0:
    print('Norte')
  elif pos_vaga == 1:
    print('Leste')
    #vet_map[][]
    direcaoDeIda(esta_i + 1,esta_j)#Nova posição que está
  elif pos_vaga == 2:
    print('Sul')
  elif pos_vaga == 3:
    print('Oeste')
  else:
    print('Todas adjacencias Oculpadas')

map_atualiza = mapa()
mapa()
mover(1,1)