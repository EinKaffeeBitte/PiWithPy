divprec = int(input("Division Precision: "))

def div(b, prec):
    prec = int(prec)
    prec -= 1
    preci = 0

    # Define a var for the answer
    ans = []

    # Define a function to convert list to float
    def l2f(lis):
        print(lis)
        lis = list(lis)
        ll = len(lis)
        text = ""
        i = 0
        while ll > 0:
            text += str(lis[i])
            i += 1
            ll -= 1
        n = float(text)
        return n


    # Define a function to convert int to list
    def i2l(inte):
        inte = str(inte)
        string = list(inte)
        return string


    a = 4
    b = int(b)
    temp1 = 0 # the result of how many times b gets into a
    temp3 = 0 # temp3 * b = temp1
    temp4 = a


    # Start, check how many times (temp1)
    # B gets into A
    while not temp1 > temp4:
        temp1 += b
    if temp1 > temp4:
        temp1 -= b

    temp3 = temp1 / b
    temp3 = int(temp3)
    print("temp1: " + str(temp1))
    print("TEMP3 " + str(temp3))
    ans.append(str(temp3) + ".")

    temp4 -= temp1 # the new a num
    temp4 = temp4 * 10
    print("New A num: " + str(temp4))
    print("ANS: " + str(ans))
    if temp4 == 0:
        return l2f(ans)

    while not preci > prec:
        temp1 = 0; temp3 = 0
        while not temp1 > temp4:
            temp1 += b
        if temp1 > temp4:
            temp1 -= b
    
        temp3 = temp1 / b
        temp3 = int(temp3)
        print("temp1: " + str(temp1))
        print("TEMP3 " + str(temp3))
        ans.append(str(temp3))
        temp4 -= temp1
        temp4 = temp4 * 10
        print("New A num: " + str(temp4))
        print("ANS: " + str(ans))
        if temp4 == 0:
            return l2f(ans)
        preci += 1


    answer = l2f(ans)
    print("Answer: " + str(answer))
    return answer


pii = 4/1
d = 3
op = False

n = input("Iterations: ")
n = int(n)
i = 0

while i <= n:
    if op == False:
        pii = pii - div(d, divprec)
    if op == True:
        pii = pii + div(d, divprec)
    
    if op == False:
        op = True
    else:
        op = False
        
    d = d + 2
    i = i + 1
print(pii)