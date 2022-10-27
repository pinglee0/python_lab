import matplotlib.pyplot as plt
def fx(x):
    return pow(x,3)+ pow(x,2)+x+1
def average(x):
    return sum(x)/len(x)
def variance(x):
    ax=average(x)
    sum=0
    for i in x:
        sum+=(i-ax)*(i-ax)
    variance=sum/len(x)
    return variance

if __name__ == '__main__':
    x=[]
    y=[]
    for i in range(41):
        x.append(-20+i)
        y.append(fx(-20+i))
    ay=average(y)
    vy=variance(y)
    print("x:",x)
    print("y:",y)
    print("average:",ay,"\nvariance:",vy)
    plt.plot(x, y, "-o")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

