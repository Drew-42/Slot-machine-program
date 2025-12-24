import random
import time

# The important functions were defined before and outside of main():

def spin_row():
	symbols = ['🍒', '🍉', '🍋', '🔔', '🌟']

	return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
	print('------------------')
	print('((' + ' | '.join(row) + '))')
	print('------------------')

def get_payout(row, bet, balance):
	if row[0] == row[1] == row[2]:
		if row[0] == '🍒':
			return bet * 3
		elif row[0] == '🍉':
			return bet * 4
		elif row[0] == '🍋':
			return bet * 5
		elif row[0] == '🔔':
			return bet * 10
		elif row[0] == '🌟':
			return bet * 20
	else:
		return 0

# The main() function that contains the main code of the python file:

def main():

# The user starts out with a balance of 100 currency units, and the main menu is printed:

	balance = 100

	print('--------------------------------------------------')
	print('    [Welcome to The Great Python Slot Machine]')
	print('--------------------------------------------------')
	print()
	print('Symbols: 🍒 🍉 🍋 🔔 🌟')
	print()
	print('--------------------------------------------------')

# The game runs only if the user has a positive balance. Once it reaches 0, the While loop 
# breaks and a 'game over' screen will be displayed:

	while balance > 0:

# The program displays the current balance and asks the user for the amount of money to 
# bet with:

		print()
		print(f'Current balance: ${balance:.2f}')

		bet = input('Place your bet amount (q to quit): ').lower()

		if bet == 'q':
			break

# Error control:			

		try:
			bet = float(bet)
		except ValueError:
			print('The value is invalid (must be numeric). Try again')
			continue

		if bet <= 0:
			print('The value is invalid (not positive). Try again')
			continue
		elif bet > balance:
			print('The value is invalid (exceeds balance). Try again')
			continue

# Here the player may choose to spin, or to bet with a different sum of money, or to quit:

		lever = input(f'You placed ${bet}. Spin (any key; n to place another bet; q to quit)?: ').lower()

		if lever == 'q':
			break
		elif lever == 'n':
			continue

# For placing the bet and receiving the payout I used the round() function because I was 
# getting floating-point precision errors that didn't allow the game to close when the value 
# reached 0.


		balance = round(balance - bet, 2)

		row = spin_row()

		print()

		for num in range(3):
			print('Spinning...\n')
			time.sleep(1)

		print_row(row)

		print()

		payout = get_payout(row, bet, balance)
		
		if payout:
			print(f'Congratulations, you WON ${payout}!')
		else:
			print('You lost this round. You didn\'t receive any money')

		balance = round(balance + payout, 2)

		if balance > 0:
			print('TRY AGAIN?')
		else:
			print('It appears you run out of money! Thanks for playing')

# The 'game over' screen:

	print('\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
	print('          <<< GAME OVER >>>')
	print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
	print(f'Your final balance is: ${balance}')


if __name__ == '__main__':
	main()