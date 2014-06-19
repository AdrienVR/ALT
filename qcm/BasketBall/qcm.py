


def main():
    a=open("r.txt")
    ai=a.readlines()
    a.close()
    
    a=open("c.txt")
    bi=a.readlines()
    a.close()

    h=[]
    for x in ai:
        h.append(x)

    a=open("t.txt","w")
    for x in h:
        a.write(x+"\n")
    a.close()
