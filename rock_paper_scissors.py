import random
def play():
    user =input("choose 'r' for rock ,'p' for paper and ,'s' for scissors :")
    
    computer = random.choice(['r','p','s'])
    if user == computer:
        return 'tie'
    if is_win(user,computer):
        return 'u won!'
    return'u loose'
def is_win(x,o):
        #x=>player ,o=>opponent
    if (x=='r' and o=='s') or (x=='s'and o=='p') or (x=='p' and o=='r'):
        return True
print(play())