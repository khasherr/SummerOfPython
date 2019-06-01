
def find_unique(list):
        for i in range(0, len(list)):
            for j in range(1, len(list)):
                if(list[i]== list[j] and i != j): #checks for counter 
                    break
                else:
                   # return list[i]
                    return list[i]


number_of_input = int(input())
list = [int (x) for x in input().split(' ')]
number = find_unique(list)
print(number);