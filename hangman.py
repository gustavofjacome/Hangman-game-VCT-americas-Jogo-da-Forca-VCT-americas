import random
from bagre import bagre_list
from hangman_visual import lives_visual_dict
import string


def get_valid_word(bagre_list):
    bagre = random.choice(bagre_list)  
    while '-' in bagre or ' ' in bagre:
        bagre = random.choice(bagre_list)

    return bagre.upper()


def hangman():
    bagre = get_valid_word(bagre_list)
    word_letters = set(bagre)  
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  

    lives = 7

   
    while len(word_letters) > 0 and lives > 0:
       
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        print('Você tem', lives, 'vidas restantes e você usou estas letras: ', ' '.join(used_letters))
        
        word_list = [letter if letter in used_letters else '-' for letter in bagre]
        print(lives_visual_dict[lives])
        print('Current word: \nPalavra atual', ' '.join(word_list))

        user_letter = input('Guess a letter: \nDigite a letra: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  
                print('\nYour letter,', user_letter, 'is not in the word.')
                print('\nA letra,', user_letter, 'não está no nome do bagre.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')
            print('\nA letra ja foi usada, tente usar outra.')

        else:
            print('\nThat is not a valid letter.')
            print('\nIsso não é uma letra válida.')

    
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', bagre)
        print('Você morreu, o bagre era:', bagre)
    else:
        print('You guessed the word', bagre, '!!')
        print('Você pescou o bagre', bagre, '!!')


if __name__ == '__main__':
    hangman()