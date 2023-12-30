import random
import matplotlib.pyplot as plt
from matplotlib import animation, rc


def init(Nx = 20, Ny = 20): # iniciar los mundos
    C = [[0 for j in range(Ny+2)] for i in range(Nx+2)] # mundo
    for i in range(1, Ny+1):
        for j in range(1, Nx + 1):
            C[i][j] = random.randint(0,1)
    return C
    #print(C)

def plot(C): # imprimir con graficos el mundo "C"
    plt.imshow(C)
    plt.axis('off')
    plt.gray()
    plt.show()


def iter(C):
    Ny, Nx = len(C) - 2, len(C[0]) - 2
    C2 = [[0 for j in range(Ny+2)] for i in range(Nx+2)] # mundo siguiente
    for i in range(1, Ny + 1):  # i = indice = fila
        for j in range(1, Nx + 1):  # celdas / celulas individuales || j = columna
            c = C[i][j]
            v = C[i][j + 1] + C[i][j - 1] + C[i + 1][j] + C[i - 1][j] + \
                C[i + 1][j + 1] + C[i - 1][j - 1] + C[i + 1][j - 1] + C[i - 1][j + 1]  # vecinos vivos
            if c == 0:
                if v == 3:
                    C2[i][j] = 1
                else:
                    C2[i][j] = 0
            else:
                if v == 2 or v == 3:
                    C2[i][j] = 1
                else:
                    C2[i][j] = 0
    for i in range(1, Ny + 1):  # cambiar con el mundo siguiente
        for j in range(1, Nx + 1):
            C[i][j] = C2[i][j]
    return C2


def game(C0 , MAX_IT = 10): # C0 = mundo inicial
    count = 0
    Cs = [C0]
    while count < MAX_IT:
        C = iter(C0)
        Cs.append(C)
        C0 = C
        count += 1
    return Cs

def update(i):
    ax.clear()
    ax.imshow(Cs[i], cmap="gray")
    ax.axis('off')
    return ax



rc('animation', html='html5')
C = init(Nx= 100, Ny=100)
Cs = game(C, MAX_IT=1000)
fig = plt.figure(figsize=(5,5))
ax = plt.subplot(1,1,1)
anim = animation.FuncAnimation(fig, update, frames=len(Cs), interval=150)
anim.save('mi_animacion_110.gif')
plt.close()
