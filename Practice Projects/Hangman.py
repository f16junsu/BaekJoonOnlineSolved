from random import randrange

word_list = ['apple', 'banana', 'orange']
selected_word = word_list[randrange(0, 3)]
word_status = ['_' for n in range(len(selected_word))]

while '_' in word_status:
    for c in word_status:
        print(c, end=' ')
    letter = input("\nInput Letter >> ")
    if letter in selected_word:
        print('Correct')
        for i in range(len(selected_word)):
            if selected_word[i] == letter:
                word_status[i] = letter
    else:
        print('Wrong')
    print("")

for c in word_status:
        print(c, end='')
print("\nSuccess")
        