import random;
import sys;

blanks = [];

def read ():
	f = open(sys.argv[1], "r");
	contents = f.read();
	f.close();
	return contents;

def get_word (txt):
	string = txt.split();
	secret_word = random.choice(string);
	
	return secret_word;

def display_blank (secret_word):
	i = 0;
	while i < len(secret_word):
		blanks.append('_');
		i += 1;

def user_input (prompt):
	user_input = input(prompt);
	return user_input;

def user_guess ():
	guess = user_input("Guess a letter: ");

	if guess >= 'a' and guess <= 'z' or guess >= 'A' and guess <= 'Z':
		return guess[0].lower();
	else:
		print("Invalid input");
		user_guess();

def check_word (guess, secret_word):
	i = 0;
	while i < len(secret_word):
		if guess == secret_word[i]:
			return True;
		i += 1;
	return False;

def correct_guess (guess, secret_word):
	i = 0;
	while i < len(secret_word):
		if guess == secret_word[i]:
			blanks[i] = guess;
		i += 1;

def win_lose (turns):
	i = 0;
	while i < len(blanks):
		if blanks[i] == '_' and turns < 7:
			return False;
		i += 1;
	return True;

def clear ():
	print("\033[H\033[J");

def print_spaceman (turns):
	piece1 = "";
	piece2 = "";
	piece3 = "";
	piece4 = "";
	piece5 = "";
	piece6 = "";
	piece7 = "";

	if turns > 0:
		piece1 = "   \x1b[36m^\x1b[0m ";
	if turns > 1:
		piece2 = "  \x1b[36m| |\x1b[0m";
	if turns > 2:
		piece3 = "  \x1b[36m|\x1b[0mO\x1b[36m|\x1b[0m ";
	if turns > 3:
		piece4 = "  \x1b[36m| |\x1b[0m ";
	if turns > 4:
		piece5 = " \x1b[36m<| |>\x1b[0m";
	if turns > 5:
		piece6 = " \x1b[36m^/ \^\x1b[0m";
	if turns > 6:
		piece7 = " \x1b[31mV\x1b[33mv\x1b[31mV\x1b[33mv\x1b[31mV\x1b[0m";

	print("| " + piece1 + "\n| " + piece2 + "\n| " + piece3 + "\n| " + piece4 + "\n| " + piece5 + "\n| " + piece6 + "\n| " + piece7 + "\n|___________");

def print_board (invalid_guess, turns):
	print("Guesses:");
	for i in invalid_guess:
		print(i, end=' ');
	print('\n');
	print("Secret Word:"); 
	for j in blanks:
		print(j, end=' ');
	print('\n');
	print("Incorrect Guesses: " + str(turns)); 

def game_loop ():
	clear();
	string = read();
	secret_word = get_word(string);
	invalid_guess = [];
	turns = 0;
	display_blank(secret_word);
	print_spaceman(turns);
	print_board(invalid_guess, turns);
	while win_lose(turns) == False:
		guess = user_guess();
		if check_word(guess, secret_word) == True:
			correct_guess(guess, secret_word);
			clear();
		else:
			invalid_guess.append(guess);
			turns += 1;
			clear();
		print_spaceman(turns);
		print_board(invalid_guess, turns);

game_loop();
