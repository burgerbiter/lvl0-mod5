"""
Create algorithms and use to solve
https://central.jointheleague.org/levels/Level0/Recipes/ForLoopGauntlet.html
"""


if __name__ == '__main__':
    for i in range(100):
        print(i)
    for i in range(100):
        print(100-i)
    for i in range(102):
        if i % 2 ==0:
            print(i)
    for i in range(100):
        if i % 2 ==1:
            print(i)
    for i in range(500):
       if i % 2 ==0:
            print(str(i) + " is even")
       elif i % 2 ==1:
            print(str(i)+ " is odd")
    for i in range(778):
        if i % 7 ==0:
            print(i)
    for i in range(15):
        print("in "+ str(i+2008) + " I was "+ str(i+1) + " years old")
    for i in range(3):
        for x in range(3):
            print(str(i)+str(x))

    for x in range(3):
        print(str(x*3+1)+str(x*3+2)+str(x*3+3))
    for i in range(10):
        print(str(i*10+1)+" "+str(i*10+2)+" "+str(i*10+3)+" "+str(i*10+4)+" "+str(i*10+5)+" "+str(i*10+6)+" "+str(i*10+7)+" "+str(i*10+8)+" "+str(i*10+9)+" "+str(i*10+10))


    pass
