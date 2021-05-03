import json
import sys

# Prime Finite Projective Plane Order [primes]
order = 5
count = 0

grid = []
vp = []
cards = []

mains = []

def calcMain():
    c0 = cards[0]
    c1 = []
    c2 = []

    for m in range(0, count):
        mains.append(-1)

    # C0
    c0a = c0.split(",")
    c0m = int(c0a[0])
    if mains[0] == -1:
        mains[0] = c0m
    else:
        print("Error C0")
        exit(1)

    # C1
    x = 1
    for i, c in enumerate(cards):
        tmp = c.split(",")
        tmp = [int(n) for n in tmp]
        if (c0m in tmp) and (c != c0):
            fc0 = c0a[x]
            x += 1
            cXa = c.split(",")
            cXm = int(cXa[1])
            if mains[i] == -1:
                mains[i] = cXm
            else:
                print("Error C1")
                exit(1)
            c1.append({"ind":i, "crd":c, "fc0":int(fc0), "main": cXm})

    # C2
    for c1c in c1:
        x1 = c1c["fc0"]
        x2 = c1c["main"]
        cds = c1c["crd"].split(",")
        cds = [int(n) for n in cds]
        for x0 in cds:
            for i, c in enumerate(cards):
                tmp = c.split(",")
                tmp = [int(n) for n in tmp]
                if (x0 in tmp) and (x1 in tmp) and (c != c0):
                    if x0 == x2:
                        if mains[i] == -1:
                            mains[i] = x1
                        else:
                            print("Error C2")
                            exit(1)
                    else:
                        if mains[i] == -1:
                            mains[i] = x0
                        else:
                            print("Error C2")
                            exit(1)


def doubleCheck():
    for c1 in cards:
        t1 = c1.split(",")
        for c2 in cards:
            if c2 != c1:
                t2 = c2.split(",")
                cnt = 0
                for i in t2:
                    if i in t1:
                        cnt += 1
                if cnt != 1:
                    # print("---- ",c2, c1, cnt) 
                    exit(1)
    print("s'all good!")

def main():

    # Total Cards
    global count
    count = (order*order) + order + 1

    # Initialize GRID
    for i in range(0, order):
        d2 = []
        for j in range(0,order):
            d2.append("")
        grid.append(d2)

    # Initialize Vanishing Points
    for i in range(0, order+1):
        vp.append(str(count -1)+",")

    symbol = 0
    for i in range(0,order):
        o = 0
        for y in range(0,order):
            vp[i] = vp[i] + str(symbol) + ","
            yi = o
            for x in range(0,order):
                grid[x][yi] += str(symbol) + ","
                yi = (yi + i) % order;
            o = o + 1
            symbol = symbol + 1

    for y in range(0,order):
        vp[order] = vp[order] + str(symbol) + ","
        for x in range(0,order):
            grid[y][x] += str(symbol) + ","
        symbol = symbol + 1

    # Flatten
    for x in range(0, order):
        for y in range(0, order):
            tmp = grid[x][y].strip(",").split(",")
            tmp = [int(n) for n in tmp]
            tmp.sort()
            tmp = [str(n) for n in tmp]
            cards.append(",".join(tmp))
    for i in range(0, order + 1):
        tmp = vp[i].strip(",").split(",")
        tmp = [int(n) for n in tmp]
        tmp.sort()
        tmp = [str(n) for n in tmp]
        cards.append(",".join(tmp))

    cards.sort()
    doubleCheck()
    #print(cards)
    calcMain()

    outJson = []
    for i in range(0, count):
      outJson.append({"card": mains[i], "list": cards[i]})
    #print(outJson)
    
    with open("order-" +str(order)+ ".json", "w") as f:
      json.dump(outJson, f)

if __name__ == '__main__':
    try:
        cnt = len(sys.argv) - 1
        if cnt == 1:
            order = int(sys.argv[1])
    except IndexError:
        print("m")
        main()

    main()
    
  

