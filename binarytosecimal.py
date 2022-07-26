def BinaryDecimal(n):  
    num, dec, base = n, 0, 1
     
    len1 = len(num)
    for i in range(len1 - 1, -1, -1):
        if (num[i] == '1'):     
            dec += base
        base = base*2;
    return dec
 

num = input('Enter a binary number: ')


print('The decimal value is =', BinaryDecimal(num))