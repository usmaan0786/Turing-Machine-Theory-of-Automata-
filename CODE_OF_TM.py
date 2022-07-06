string = input("Please Enter String: ")

length = len(string) + 2

tape = length * ['B']

i = 1

tapehead = 1

for s in string: #loop to place string in tape
    tape[i] = s
    i += 1

state = 0
#assigning characters to variable so that don't have to use characters each time
accept = False

def action(input_char, replace_with, move, new_state):
    global tapehead, state
    if tape[tapehead] == input_char:
        tape[tapehead] = replace_with
        state = new_state
        if move == 'L':
            tapehead -= 1
            return True
        elif move == 'R':
            tapehead += 1      
            return True
    return False

oldtapehead = -1

while(oldtapehead != tapehead): 
    oldtapehead = tapehead
    print(tape , "with tapehead at Node", tapehead, "on state" , state)
    
    if state == 0:
        if action('a', 'X', 'R', 1) or action('Y', 'Y', 'R', 8):
            pass
        
    elif state == 1:
        if action('a', 'a', 'R', 1) or action('Y', 'Y', 'R', 1) or action('b','Y','R',2):
            pass
        
    elif state == 2:
        if action('b', 'Y', 'R', 3):
            pass
            
    elif state == 3:
        if action('b', 'b', 'R', 3) or action('c', 'Z', 'R', 4) or action('Z', 'Z', 'R', 3):
            pass

    elif state == 4:
        if action('c', 'Z' , 'R', 5):
            pass
            
    elif state == 5:
        if action('c', 'Z', 'L', 6):
            pass    

    elif state == 6:
        if action('Z', 'Z', 'L', 7):
            pass

    elif state == 7:   
        if action('a', 'a' , 'L' , 7 ) or action('Y', 'Y', 'L' ,7) or action('Z', 'Z', 'L' , 7) or action('b', 'b', 'L' , 7) or action('X', 'X', 'R' , 0) :
            pass        
    
    elif state == 8:
        if action('Y', 'Y', 'R', 8) or action('Z', 'Z', 'R', 8) or action('B', 'B', 'R', 9):
            pass  

    elif state == 9:
        accept = True

    else: 
        accept = False
        
            
if accept:
    print("String accepted on state = ", state)
else:
    print("String not accepted on state = ", state)