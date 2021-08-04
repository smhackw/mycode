#!/usr/bin/env python3

round = 0

while True:
    round = round + 1

    print('finish the movie title, "Monty Python\'s The Life of      "')

    answer = input("your guess: ")

    if answer == 'Brian':
        print('correct')

        break

    elif round ==3:
        print("sorry, the answer was Brian.")

        break
    else:
        print("sorry! try again!")


