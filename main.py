import random
def is_win(user,computer):
    return ((user=='p' and computer=='r') or (user=='s' and computer=='p') or (user=='r' and computer=='s'))
def play():
    user=input("make your choice! 'r' for Rock 's' for scissors 'p' for paper or press any key to exit\n" )
    while user in ['r','p','s']:
        computer=random.choice(['r','p','s'])
        if user==computer:
            print("Match Tied\n")
        elif is_win(user,computer):
            print("You won\n")
        else:
            print("You lost\n")
        user=input("make your choice! 'r' for Rock 's' for scissors 'p' for paper or press any key to exit\n" )
play()
print("Thanks for playing!")
