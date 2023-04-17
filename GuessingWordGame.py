import random

words = ['camel', 'sylhet', 'water']

select_word = random.choice(words)
# print(select_word)
display = []

for _ in range(len(select_word)):
    display += '_'
# print(display)
should_continue = True

lives = 6

while should_continue:

    guess = input("Enter a letter: ").lower()

    if guess in display:
        print(f'you already guessed {guess}')

    for position in range(len(select_word)):
        letter = select_word[position]
        if guess == letter:
            display[position] = letter

    if guess not in select_word:
        lives -= 1
        if lives == 0:
            should_continue = False
            print('You lose')

    print(display)
    if '_' not in display:
        should_continue = False
        print("You won!")