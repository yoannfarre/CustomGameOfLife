import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


### INIT UNIVERSE ###
def compute_u(n):
    u_i = 42
    for index in range(n):
        u_i = compute_u_next(u_i)

    #print("Result for n = " + str(n) + " : " + str(u_index))
    return u_i

def compute_u_next(u_i):
    following_member = (16383 * u_i) % 59047
    return following_member



def compute_v(i):
    u_index = compute_u(i)
    u = u_index % 3
    v_index = 0
    if (u == 0):
        v_index = 1
    return v_index

################# UNIVERSE #################

def display_universe(universe):
    print (universe)

def generate_universe(k):
    universe = np.full((k, k), 0)
    counter = 0
    for i in range(k):
        for j in range(k):
            v = compute_v(i+(j*k))
            if (v == 1):
                universe[i, j] = 1
                counter += 1

    #display_universe(universe)
    print("Living cells : " + str(counter))
    return universe

def getLivingCellsNumber(universe):
    dim = universe.shape[0]
    counter = 0
    for i in range(dim):
        for j in range(dim):
            if universe[i,j] == 1:
                counter += 1
    return counter

def evolve(universe):
    dim = universe.shape[0]
    #print("Dimension : " + str(dim))
    new_universe = np.full((dim, dim), 0)
    for i in range(dim):
        for j in range(dim):
            if (universe[i, j] == 1):
                livingCells = getAroundLivingCellsNumber(universe, dim, i, j)
                if (livingCells == 2 or livingCells == 3):
                    new_universe[i, j] = 1
                else:
                    new_universe[i, j] = 0
            else:
                livingCells = getAroundLivingCellsNumber(universe, dim, i, j)
                if (livingCells == 3):
                    new_universe[i, j] = 1
                else:
                    new_universe[i, j] = 0

    return new_universe

def getAroundLivingCellsNumber(universe, dim, i, j):
    ip_jp = universe[(i+1)%dim, (j+1)%dim]
    ip_j = universe[(i+1)%dim, (j)%dim]
    ip_jm = universe[(i+1)%dim, (j-1)%dim]
    i_jp = universe[(i)%dim, (j+1)%dim]
    i_j = universe[(i)%dim, (j)%dim]
    i_jm = universe[(i)%dim, (j-1)%dim]
    im_jp = universe[(i-1)%dim, (j+1)%dim]
    im_j = universe[(i-1)%dim, (j)%dim]
    im_jm = universe[(i-1)%dim, (j-1)%dim]

    #Do not take into account i,j
    sum = ip_jp + ip_j + ip_jm + i_jp + i_jm + im_jm + im_j + im_jp
    return sum

################# TESTS #################

def test1():
    print("TEST 1")
    print("n = 996, result : " + str(compute_u(996)))
    print("n = 9996, result : " + str(compute_u(9996)))

def test2():
    print("TEST 2")
    counter = 0
    for i in range(10000):
        vi = compute_v(i)
        if (vi == 0):
            counter += 1
    print("Number of solution for vi = 0 : " + str(counter))

def test3():
    print("TEST 3")
    generate_universe(20)
    generate_universe(50)

def test4():
    print("TEST 4")
    #universe = generate_universe(20)
    universe = generate_universe(50)
    for t in range(10):
        universe = evolve(universe)
        print("Living cells : " + str(getLivingCellsNumber(universe)))
    plt.matshow(universe)
    plt.show()

def test5():
    print("TEST 5")
    fig, ax = plt.subplots()
    global g_universe
    g_universe = generate_universe(50) # ici k = 50
    global mat
    mat = ax.matshow(generate_data())
    ani = FuncAnimation(fig, update, data_gen, interval=1)
    plt.show()

"""
test1()
test2()
test3()
test4()
test5()
"""

################# ANIMATION #################

def data_gen():
    while True:
        yield generate_data()

def update(data):
    mat.set_data(data)
    return mat

def generate_data():
    global universe
    universe = evolve(universe)
    return universe

# Animation Script

fig, ax = plt.subplots()
universe = generate_universe(150) # Size
mat = ax.matshow(generate_data())
ani = FuncAnimation(fig, update, data_gen, interval=1)
plt.show()



