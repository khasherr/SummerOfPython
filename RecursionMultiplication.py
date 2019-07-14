#Sher
#This program does multuplication recursivelu

def muliplication(m,n):
    if m == 0 or n == 0: #either m or n = 0 returns 0 bc 0 * anything == 0
        return 0
    else:
        # IH - give me the multiplication of m * (n-1) meaning that if i want to find multiplication of
        # 3 *2 --> (m ==3, n ==2) so what this code is saying give me multuplication of 3 * 1 which is 3
        # and then i will add m to it -- so in the xample i will add 3 to the result
        # 1)we want ot find 3*2 which is 6
        # 2) give me result of 3*1 == which is 3
        # 3) now i will add m to it whihc in this case is 3 -- 3+3 --> 6
     smallNumber = m *(n-1)
    return smallNumber + m

m = int(input())
n = int(input())
print(muliplication(m,n))
