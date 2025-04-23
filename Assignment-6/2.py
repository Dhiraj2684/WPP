import random

class Rock_paper_scissors:
    def __init__(self,total_rounds):
        self.total_rounds = total_rounds
        self.current_round = 0
        self.user_wins = 0
        self.comp_wins = 0
        self.choices = ['rock','paper','scissor']

    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def get_user_choice(self):
        choice = input("Enter your choice(rock,paper,scissor): ").lower()
        while choice not in self.choices:
            choice = input("Invalid choice!\nPlease Enter correct Choice: ").lower()
        return choice
    
    def det_round_winner(self,user_choice,computer_choice):
        if(user_choice == computer_choice):
            return "Tie!"
        elif(user_choice == 'rock' and computer_choice == 'scissor' or
             user_choice == 'paper' and computer_choice == 'rock' or
             user_choice == 'scissor' and computer_choice == 'paper'):
            return "user"
        else:
            return "computer"
        
    def play_round(self):
        if(self.current_round < self.total_rounds):
            self.current_round += 1
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            print(f"Round: {self.current_round}: You- {user_choice}, Computer- {computer_choice}")
            winner = self.det_round_winner(user_choice,computer_choice)
            if winner == 'user':
                self.user_wins += 1
                print("You win this round!")
            elif winner == 'computer':
                self.comp_wins += 1
                print("Computer wins this round!")
            else:
                print("It's a tie!")
        else:
            print("Game Over!")
    
    def game_winner(self):
        if(self.current_round >= self.total_rounds):    
            if(self.user_wins > self.comp_wins):
                print("You won the game!")
            elif(self.user_wins < self.comp_wins):
                print("Computer won the game!")
            else:
                print("The Game ended in Draw!")

    def play_game(self):
        while self.current_round < self.total_rounds:
            self.play_round()
        self.game_winner()
        print(f"Final Score - You: {self.user_wins}, Computer: {self.comp_wins}")

rounds = int(input("Enter number of rounds: "))
game = Rock_paper_scissors(rounds)
game.play_game()