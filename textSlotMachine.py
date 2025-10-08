MAX_LINES=3
MAX_BET=100
MIN_BET=1
def deposit():
    while True:
        amount=input("What would you like to deposit? : Rs.")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Please enter a positive number.")
        else:
            print("Please enter a number.")
    return amount
def get_number_of_lines():
    while True:
        lines=input("Enter the number of lines to bet on (1-"+ str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines
def get_bet():
    while True:
        bet=input("How much would you like to bet on each line? Rs.")
        if bet.isdigit():
            bet=int(bet)
            if MAX_BET4<=bet<=MAX_BET:
                break
            else:
                print(f"Please enter a number between Rs.{MIN_BET} - Rs.{MAX_BET}.")
        else:
            print("Please enter a number.")
    return bet
def main():
        balance=deposit()
        lines=get_number_of_lines()
        bet=get_bet()
        
        print(f"Your balance is Rs.{balance}.")

main()
