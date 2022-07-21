# A stack to store salaries of employees is implemented using lists. Write the python code to show the pop operation in this stack using .	
salaries = [50000,80000,47000,100000]

def isEmpty(stack):
    if len(stack)==0:
        return True
    else:
        return False

def push(stack,item):
    stack.append(item)

def pop(stack):
    e = stack.pop()
    return e

def length(stack):
    return len(stack)

print(salaries)
print("popping salaries...")
item = pop(salaries)
print("Popped salary: ",item,"Salary Stack: ",salaries)
    
