import numpy as np
def chk_simp_opt(tab):
    j = (np.argmin(tab[0, 1:]))+1
    if(tab[0][j])>=0:
        return True
    
    return False

def chk_dual_opt(tab):
    i = (np.argmin(tab[1:, 0]))+1
    if(tab[i][0])>=0:
        return True
    
    return False
    
def add_gomory(tab, i):
    #Add gomory cut of i source to tableau tab
    pass

def dual_simplex_iter(M, tab):
    #Perform dual simplex iteration on tableau tab
    pass

def simplex_iter(M, tab):
    m,n = np.shape(tab)
    # i,j are coordinates of pivot element
    j = (np.argmin(tab[0,1:]))+1
    
    minval = float('inf')
    for t in range(1,m):
        if(tab[t][j]>0):
            if(tab[t][0]/tab[t][j]<=minval):
                minval = tab[t][0]/tab[t][j]
                i=t
    M[i-1] = j
    tab[i,:] = (tab[i,:])/tab[i,j]
    for k in range(m):
        if(k!=i):
            tab[k,:] = tab[k,:] - (tab[i, :])*tab[k][j]

    return M,tab

def load(filename):
    with open('test.txt', 'r') as fd:
        reader = fd.readlines()
        n,m = map(int, reader[0].split(" "))
        b = list(map(int, reader[1].split(" ")))
        c = list(map(int, reader[2].split(" ")))
        a = []
        for i in range(m):
            a.append(list(map(int, reader[3+i].split(" "))))
    return n,m,b,c,a

def gomory(filename):
    n,m,b,c,a = load(filename)  
    tab = create_tableau(n,m,b,c,a)

    # M is list of basic indices, in 1 indexed form
    M = [i for i in range(n,n+m)]

    while(not chk_simp_opt(tab)):
        M, tab = simplex_iter(M, tab)

    return tab
    
    while(True):
        flag=0
        frac = 0
        #Find fractional basic variable
        for i in M:
            if (tab[0][i] - int(tab[0][i]))!=0:
                flag=1
                frac = i
                break
        if(flag==0):
            return tab[0][M]
        
        tab = add_gomory(tab, i)
        while(not chk_dual_opt(tab)):
            M, tab = dual_simplex_iter(M, tab)


    # Take input from file "filename"
    #return x # an array of n integers

def create_tableau(n,m,b,c,a):
    c = -1*np.hstack((c, np.zeros(m)))
    tab = a
    tab = np.hstack((tab, np.zeros((m,m))))
    for i in range(m):
        tab[i][i+n] = 1
    tab = np.vstack((c, tab))
    b.insert(0,0)

    b1 = []
    for i in b:
        b1.append([i])
    b = b1

    tab = np.hstack((b, tab))
    return tab

print(gomory('test.txt'))



'''Maximize z = x1 + 4x2
subject to
2x1 + 4x2 ≤ 7
5x1 + 3x2 ≤ 15
x1, x2 are integers ≥ 0'''



        
