import math

chooseMethod = int(input("Enter method  1)Secant 2)Modified Secant 3)Fixed point 4)Newton Raphson: "))

if chooseMethod ==1:
    # input the function data
    xPower3 = float(input("Enter X^3: "))
    xPower2 = float(input("Enter X^2: "))
    xPower1 = float(input("Enter X: "))
    coeff = float(input("Enter Cofficent C= "))
    tol = float(input("Enter tolerence "))
    range1 = float(input("Enter range1: "))
    range2 = float(input("Enter range2: "))

    # get number of iterations
    m = math.log((range2 - range1) / tol) / math.log(2)
    iterations = math.ceil(m)
    print("The number of iterations (N) : ", iterations)

    # getting first row data
    a = []
    a.append(range1)
    b = []
    b.append(range2)
    functAarray = []
    functBarray = []
    functCarray = []
    compare = []
    iEqualN = []
    functA = (xPower3 * math.pow(a[0], 3)) + (xPower2 * math.pow(a[0], 2)) + (xPower1 * math.pow(a[0], 1)) + coeff
    functAarray.append(functA)
    functB = xPower3 * math.pow(b[0], 3) + xPower2 * math.pow(b[0], 2) + xPower1 * math.pow(b[0], 1) + coeff
    functBarray.append(functB)
    c = []
    n1 = b[0] - a[0]
    n2 = functBarray[0] - functAarray[0]
    num = b[0] - functBarray[0] * (n1 / n2)
    c.append(num)
    functC = xPower3 * math.pow(c[0], 3) + xPower2 * math.pow(c[0], 2) + xPower1 * math.pow(c[0], 1) + coeff
    functCarray.append(functC)
    compare.append("false")
    iEqualN.append("false")
    counter = 1

    for i in range(1, iterations):
        a.append(b[i - 1])
        b.append(c[i - 1])
        functAarray.append(functBarray[i - 1])
        functBarray.append(functCarray[i - 1])
        n1 = b[i] - a[i]
        n2 = functBarray[i] - functAarray[i]
        num = b[i] - functBarray[i] * (n1 / n2)
        c.append(num)
        functC = xPower3 * math.pow(c[i], 3) + xPower2 * math.pow(c[i], 2) + xPower1 * math.pow(c[i], 1) + coeff
        functCarray.append(functC)
        counter = counter + 1
        if i != iterations:
            iEqualN.append("false")
        else:
            iEqualN.append("true")
        if abs(functCarray[i]) < tol:
            compare.append("true")
            break
        else:
            compare.append("false")
            continue

    for j in range(0, counter):
        print(
            f"{round(j, 4)} : {round(a[j], 4)}: {round(b[j], 4)} :{round(c[j], 4)} : {round(functAarray[j], 4)} : {round(functBarray[j], 4)} : {round(functCarray[j], 4)} : {compare[j]}: {iEqualN[j]} ")

    approximateRoot = c[counter - 1]
    print("The approximate root is :", approximateRoot)

#------------------------------------------------------Modified Secant----------------------------------------------------------------------
if chooseMethod ==2:
    # input the function data
    xPower3 = int(input("Enter X^3: "))
    xPower2 = int(input("Enter X^2: "))
    xPower1 = int(input("Enter X: "))
    coeff = int(input("Enter Cofficent C= "))
    tol = float(input("Enter tolerence "))
    range1 = int(input("Enter range1: "))
    range2 = int(input("Enter range2: "))

    # get number of iterations
    m = math.log((range2 - range1) / tol) / math.log(2)
    iterations = math.ceil(m)
    print("The number of iterations (N) : ", iterations)

    # getting first row data
    a = []
    a.append(range1)
    b = []
    b.append(range2)
    functAarray = []
    functBarray = []
    functCarray = []
    compare = []
    iEqualN = []
    functA = xPower3 * math.pow(a[0], 3) + xPower2 * math.pow(a[0], 2) + xPower1 * math.pow(a[0], 1) + coeff
    functAarray.append(functA)
    functB = xPower3 * math.pow(b[0], 3) + xPower2 * math.pow(b[0], 2) + xPower1 * math.pow(b[0], 1) + coeff
    functBarray.append(functB)
    c = []
    num = b[0] - functB * ((b[0] - a[0]) / (functB - functA))
    c.append(num)
    functC = xPower3 * math.pow(c[0], 3) + xPower2 * math.pow(c[0], 2) + xPower1 * math.pow(c[0], 1) + coeff
    functCarray.append(functC)
    compare.append("false")
    iEqualN.append("false")
    root = []
    appRoot = 0
    if functCarray[0] > 0 and functAarray[0] < 0:
        root.append("c&a")
    else:
        root.append("c&b")

    counter = 1
    # Loop for getting data
    for i in range(1, iterations):

        if root[i - 1] == "c&b":
            a.append(c[i - 1])
            b.append(b[i - 1])
            functAarray.append(functCarray[i - 1])
            functBarray.append(functBarray[i - 1])
            num = b[i] - functBarray[i] * ((b[i] - a[i]) / (functBarray[i] - functAarray[i]))
            c.append(num)
            functC = xPower3 * math.pow(c[i], 3) + xPower2 * math.pow(c[i], 2) + xPower1 * math.pow(c[i], 1) + coeff
            functCarray.append(functC)
            counter = counter + 1
            if functCarray[i] > 0 and functAarray[i] < 0:
                root.append("c&a")
                iEqualN.append("false")
            else:
                root.append("c&b")
                iEqualN.append("false")

            if abs(functCarray[i]) < tol:
                compare.append("true")
                break
            else:
                compare.append("false")
                continue

        else:
            a.append(a[i - 1])
            b.append(c[i - 1])
            num = b[i] - functBarray[i] * ((b[i] - a[i]) / (functBarray[i] - functAarray[i]))
            c.append(num)
            functAarray.append(functAarray[i - 1])
            functBarray.append(functCarray[i - 1])
            functC = xPower3 * math.pow(c[i], 3) + xPower2 * math.pow(c[i], 2) + xPower1 * math.pow(c[i], 1) + coeff
            functCarray.append(functC)
            if abs(functCarray[i]) < tol:
                compare.append("true")
                break
            else:
                compare.append("false")
                continue

    # printing data
    for j in range(0, counter):
        print(
            f"{round(j, 4)} : {round(a[j], 4)}: {round(b[j], 4)} :{round(c[j], 4)} : {round(functAarray[j], 4)} : {round(functBarray[j], 4)} : {round(functCarray[j], 4)}  : {compare[j]} :{iEqualN[j]} :  {root[j]}")

    # Approximate Root
    appRoot = c[counter - 1]
    print("The approximate root is : ", round(appRoot, 4))

#------------------------------------------------Fixed point------------------------------------------------------------------------------
if chooseMethod ==3:
    # input the function data
    xPower3 = int(input("Enter X^3: "))
    xPower2 = int(input("Enter X^2: "))
    xPower1 = int(input("Enter X: "))
    coeff = int(input("Enter Cofficent C= "))
    tol = float(input("Enter tolerence "))
    x0 = int(input("Enter X0: "))
    xi = []
    xi.append(x0)

    # get number of iterations
    iterations = int(input("Number of iterations: "))

    # get f(X)
    fOfX = []
    f = (xPower3 * x0) + (xPower2 * x0) + (xPower1 * x0) + (coeff)
    fOfX.append(f)
    gOfX = []
    g = (xPower3 * x0) + (xPower2 * x0) + (xPower1 * x0) + (coeff) + x0
    gOfX.append(g)

    # get all data of table
    compare = []
    compare.append("false")
    iEqualN = []
    iEqualN.append("false")
    counter = 1
    for i in range(1, iterations):

        xi.append(gOfX[i - 1])
        f = xPower3 * math.pow(xi[i], 3) + xPower2 * math.pow(xi[i], 2) + xPower1 * math.pow(xi[i], 1) + coeff
        fOfX.append(f)
        g = xPower3 * math.pow(xi[i], 3) + xPower2 * math.pow(xi[i], 2) + xPower1 * math.pow(xi[i], 1) + coeff + xi[i]
        gOfX.append(g)
        counter = counter + 1
        if counter != iterations:
            iEqualN.append("false")
        else:
            iEqualN.append("true")
        if abs(fOfX[i]) < tol:
            compare.append("true")
            break
        else:
            compare.append("false")
            continue

    for j in range(0, counter):
        print(f"{j} : {xi[j]}: {fOfX[j]} :{gOfX[j]} :{compare[j]} :{iEqualN[j]}")

    approximateRoot = gOfX[counter - 1]
    print("The approximate root is :", approximateRoot)

#--------------------------------------------Newton Raphson-----------------------------------------------------------------------
if chooseMethod ==4:
    # input the function data
    xPower3 = int(input("Enter X^3: "))
    xPower2 = int(input("Enter X^2: "))
    xPower1 = int(input("Enter X: "))
    coeff = int(input("Enter Cofficent C= "))
    tol = float(input("Enter tolerence "))
    x0 = int(input("Enter X0: "))
    xi = []
    xi.append(x0)

    # get number of iterations
    iterations = int(input("Number of iterations: "))

    # get f(X)
    fOfX = []
    f = (xPower3 * pow(x0, 3)) + (xPower2 * pow(x0, 2)) + (xPower1 * pow(x0, 1)) + coeff
    fOfX.append(f)
    diff = []
    num = (xPower3 * 3 * pow(x0, 2)) + (xPower2 * 2 * pow(x0, 1)) + xPower1
    diff.append(num)
    # print(xi[0])
    # print(fOfX[0])
    # print(diff[0])

    # get all data of table
    compare = []
    compare.append("false")
    iEqualN = []
    iEqualN.append("false")
    counter = 1
    for i in range(1, iterations):
        getNextNum = xi[i - 1] - (fOfX[i - 1] / diff[i - 1])
        xi.append(getNextNum)
        f = (xPower3 * pow(xi[i], 3)) + (xPower2 * pow(xi[i], 2)) + (xPower1 * pow(xi[i], 1)) + coeff
        fOfX.append(f)
        n1 = (xPower3 * 3 * pow(xi[i], 2)) + (xPower2 * 2 * pow(xi[i], 1)) + xPower1
        diff.append(n1)
        counter = counter + 1
        if counter != iterations:
            iEqualN.append("false")
        else:
            iEqualN.append("true")
        if abs(fOfX[i]) < tol:
            compare.append("true")
            break
        else:
            compare.append("false")
            continue

    for j in range(0, counter):
        print(
            f"{round(j, 4)} :{round(xi[j], 4)}: {round(fOfX[j], 4)} : {round(diff[j], 4)} : {compare[j]}  :{iEqualN[j]}")

    approximateRoot = xi[counter - 1]
    print("The approximate root is :", approximateRoot)

