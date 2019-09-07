#Sher
# The idea is to check if the brackets are balanced ({[ ]}) means that its balanced
# {[] is unbalanced. Every bracket must have closing bracket and must match.
# In this program implemented stack as a list - pushes bracket into stack and if match occur it pops it off
# then compares to the next item in stack compares to the top either and so on.

def check_Balanced(string):
   #stack could be implemented as a list
    s = []

    #looping everything character in a string
    for character in string:
        #if character is one of the brackets append to the stack otherwise do not we dont want aphabets or numericals in stack
        #remember the order of the brackets ( needs to be checked first
        if character in '({[':
            #append to the stack
            s.append(character)
        elif character is ")":
            #if stack is empty and the last element in the stack is not equal to ( brack
            # return false otherwise pop the element .
            #if matches pop it from the stack means that pair is no longer in the stack moves to next
            #element in stack
            if (not s or s[-1] != "("):
                return False
            s.pop()
        elif character is "}":
            if(not s or s[-1] != "{"):
                return False
            s.pop()
        elif character is "]":
            if (not s or s[-1] != "["):
                return False
            s.pop()

    #check if stack is empty return true else return false
    if (not s):
        return True
    return False



string = input()
answer  = check_Balanced(string)
print(answer)