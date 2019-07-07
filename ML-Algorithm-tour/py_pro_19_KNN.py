import matplotlib.pyplot as plt
import math

def KNN(F,L,ind_):
    f  = F
    l = L
    d = {}
    s = set(l)

    for i in s:
        L = []
        count = 0
        for j in range(len(l)):
            if i == l[j]:
                if count == 0:
                    d[i] = [L + (f[j])]
                    count = 1
                else:
                    d[i].append(f[j])
    l_k = []
    for i in d:
        l_k.append(len(d[i]))
    ind = ind_

    m = min(l_k)

    if ind > m:
        ind = m
    x_g = [] 
    y_g = []
    x_b = []
    y_b = []
    x = []
    y = []

    for i in range(len(f)):
        x.append(f[i][0])
        y.append(f[i][1])
    for i in range(len(f)):
        if l[i] == 'good' :
            x_g.append(f[i][0])
            y_g.append(f[i][1])
        elif l[i] == 'bad':
            x_b.append(f[i][0])
            y_b.append(f[i][1])

    x_g_mean = sum(x_g)//len(x_g)
    y_g_mean = sum(y_g)//len(y_g)
    x_d = []
    y_d = []

    for i in range(len(x_g)):
        x_d.append(x_g[i] - x_g_mean)
        y_d.append(y_g[i] - y_g_mean)
    x_y_2 = []
    x_2 = []

    for i in range(len(x_g)):
        x_y_2.append(x_d[i] * y_d[i])
        x_2.append(x[i]**2)
    
    slope = sum(x_y_2)//sum(x_2)
    c  = y_g_mean - (slope * x_g_mean)

    y_p = []

    for k in range(len(x_g)):
        y_p.append(x_g[k]*slope + c)
    
    plt.plot(x_g,y_p)
    plt.plot(x_g,y_g,'r*',label = 'Good')
    plt.plot(x_b,y_b,'b*',label = 'Bad')
    plt.xlabel("Habit")
    plt.ylabel("Saving")
    plt.title("KNN-Algorithm")

    x_y = []
    y_y = []
    y_pred = [[15,5],[7,7],[42,7],[4,2]]
    for i in range(len(y_pred)):
        x_y.append(y_pred[i][0])
        y_y.append(y_pred[i][1])
    plt.plot(x_y,y_y,'k^',label = 'New point')
    plt.legend()

                                
    for w in y_pred:
        x_j = w[0]
        y_j = w[1]
        D = []
        Dis = []
        iD = []
        for k in range(len(x)):
            E_d = math.sqrt((x[k] - x_j)**2 + (y[k] - y_j)**2)
            D.append(E_d)
        dis = D[:]
        for i in range(ind):
            mn = min(dis)
            Dis.append(mn)
            iD.append(dis.index(mn))
            dis.remove(mn)
        Dic = {}
        for j in d:
            Dic[j] = 0
        for i in iD:
            Dic[l[i]] = Dic[l[i]] + 1
        m_d = Dic.values()
        mx = max(m_d)
        for i in Dic:
            if Dic[i] == mx:
                print(" -> the predict: " + str(i))
                break
    plt.show()


