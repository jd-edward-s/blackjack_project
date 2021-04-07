class Chips:
    def __init__(self):
        self.balance = 0
        self.bet = 0

    def deposit(self):
        while True:
            try:
                deposit = int(input("How much would you like to credit your account with?: £ "))
                self.balance += deposit
                print("Your account has been successfully credited.")
                print(f"Account Balance: {self.balance}")
                return self.balance
                break
            except ValueError:
                print("That input wasn't recognised, please enter the value you wish to deposit in numerical form.")

    def wager(self):
        while True:
            balance = self.balance
            try:
                stake = int(input("How much would you like to bet?: £ "))
                if balance - stake >= 0:
                    self.bet += stake
                    self.balance -= stake
                    break
                else:
                    print("You have insufficient funds in your account to place that bet!")
                    decision = input("Would you like to add more funds? (enter 'y' or 'n'): ").lower()
                    if decision[0] == 'y':
                        self.deposit()
                        continue
                    else:
                        continue
            except ValueError:
                print("That input wasn't recognised, please enter the value you wish to deposit in numerical form.")


def main():
    player_chips = Chips()
    player_chips.deposit()
    player_chips.wager()
    print(f"Account Balance: {player_chips.balance}")
    print(f"Current bet: {player_chips.bet}")


if __name__ == "__main__":
    main()
