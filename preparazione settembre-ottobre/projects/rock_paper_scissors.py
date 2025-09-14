import random

def rock_paper_scissors(rounds: int):

    user_points = 0
    computer_points = 0

    if rounds <= 0:
        
        raise ValueError("si deve giocare almeno un round")

    moves: list[str] = ["sasso", "carta", "forbice"]

    for i in range(rounds):
        
        u_move: str = str(input("fai la tua mossa: "))
        c_move = random.choice(moves)

        if u_move not in moves:
            
            raise ValueError(f"la mossa: {u_move} non è tra le mosse possibili: {moves}")
        
        if u_move == "sasso" and c_move == "forbice":
            user_points += 1
        
        elif u_move == "carta" and c_move == "sasso":
            user_points += 1
        
        elif u_move == "forbice" and c_move == "carta":
            user_points += 1
        
        elif u_move == c_move:
            pass

        else:
            computer_points += 1
        
        print(f"mossa utente: {u_move}")
        print(f"mossa computer: {c_move}")
    
    if user_points > computer_points:
        print(f"vince l'utente!, punteggio utente: {user_points}, punteggio computer: {computer_points}")
    
    elif computer_points > user_points:
        print(f"vince il computer!, punteggio utente: {user_points}, punteggio computer: {computer_points}")
    
    else:
        print(f"pareggio, punteggio utente: {user_points}, punteggio computer: {computer_points}")

def main():

    rock_paper_scissors(10)

main()

            


