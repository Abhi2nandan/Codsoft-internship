import random

def play():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print(f"Computer chose: {computer_choice}")

    # Check for a tie
    if user_choice == computer_choice:
        return "It's a tie!"
    
    # Check all winning conditions
    if is_win(user_choice, computer_choice):
        return "You win!"
    
    # If it's not a tie and the user didn't win, the computer wins
    return "You lose!"

def is_win(player, opponent):
    # Return True if the player beats the opponent
    # Winning conditions: rock > scissors, scissors > paper, paper > rock
    if (player == 'rock' and opponent == 'scissors') or \
       (player == 'scissors' and opponent == 'paper') or \
       (player == 'paper' and opponent == 'rock'):
        return True
    return False

def main():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        result = play()
        print(result)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
