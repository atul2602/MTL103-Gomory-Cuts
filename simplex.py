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
    m,n = np.shape(tab)
    j = (np.argmin(tab[1:, 0]))+1
#     if !(chk_dual_opt(tab)):
    minval = float("inf")
    for k in range(1,n):
        if tab[j][k] < 0:
            if -tab[0][k]/tab[j][k] <= minval : 
                minval = -tab[0][k]/tab[j][k] 
                i = k
    M[j-1] = i #  ------------------ doubt in existence of M? -----------------
#  j,i are pivot indices
    tab[j,:] = tab[j,:]/tab[j,i]
    for z in range(m):
        if z!=j:
            tab[z,:] = tab[z,:] - (tab[j,:]*tab[z,i]
    return M,tab
    
    
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
        n,m = map(int, reader[0].rstrip('\n').split(" "))
        b = list(map(int, reader[1].rstrip('\n').split(" ")))
        c = list(map(int, reader[2].rstrip('\n').split(" ")))
        a = []
        for i in range(m):
            a.append(list(map(int, reader[3+i].split(" "))))
    return n,m,b,c,a

def simplex(n,m,tab, c):
    #Phase 1
    M = [i for i in range(n+m+1,n+2*m+1)]
    while(not chk_simp_opt(tab)):
        M, tab = simplex_iter(M, tab) 

    tab = np.array(tab)
    tbd=[]
    # for i in range(n+m+1, n+2*m+1):
    #     if(i not in M):
    #         tbd.append(i)
    
    tab = np.delete(tab, [j for j in range(n+m+1, n+2*m+1)], axis = 1)

    tbd = []
    for i in range(len(M)):
        if(M[i]>n+m):
            tbd.append(i+1)
    
    M1 = []
    for i in range(len(M)):
        if(i+1 not in tbd):
            M1.append(M[i])

    M = M1

    tab = np.delete(tab, tbd, axis = 0)
    for j in range(1,len(tab[0])):
        tab[0][j] = c[j-1] - np.dot([c[_-1] for _ in M], tab[1:,j])

    while(not chk_simp_opt(tab)):
        M, tab = simplex_iter(M, tab)

    return M, tab

    
    
def gomory(filename):
    n,m,b,c,a = load(filename)  
    tab, c = create_tableau(n,m,b,c,a)

    # M is list of basic indices, in 1 indexed form
    M = [i for i in range(n+m,n+2*m)]

    M, tab = simplex(n, m, tab, c)

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
        
        tab = add_gomory(tab, frac)
        while(not chk_dual_opt(tab)):
            M, tab = dual_simplex_iter(M, tab)


    # Take input from file "filename"
    # return x # an array of n integers

def create_tableau(n,m,b,c,a):
    c = np.array(c)
    c = -1*np.hstack((c, [0 for i in range(m)]))   #like a minimisation problem
    c1 = np.zeros((1, n+2*m))     #for auxiliary problem
    
    tab = a
    tab = np.hstack((tab, np.zeros((m,2*m))))

    for i in range(m):
        tab[i][i+n] = 1
        if(b[i]<0):
            tab[i] = -1*tab[i]
            b[i] = -1*b[i]
        tab[i][i+n+m] = 1
    
    #Configuring reduced costs for x, and s
    c1[0][:n+m] = -1*np.sum(tab[:, :n+m], axis = 0)
    
            
    tab = np.vstack((c1, tab))
    b.insert(0,0)

    b1 = []
    for i in b:
        b1.append([i])
    b = b1

    tab = np.hstack((b, tab))
    return tab, c

print(gomory('test.txt'))



'''Maximize z = x1 + 4x2
subject to
2x1 + 4x2 ≤ 7
5x1 + 3x2 ≤ 15
x1, x2 are integers ≥ 0'''



        
