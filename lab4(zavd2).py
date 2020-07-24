word = "London is a capital of Great Britain"
vowels = set("aeiouy")
word_set = set(word.lower())
 
print('Голосних {}, Приголосних {}'.format(len(word_set.intersection(vowels)),
                                        len(word_set.difference(vowels))))

if len(word_set.intersection(vowels)) > len(word_set.difference(vowels)):
    print ('Голосних більше')
else:
        print ('Приголосних більше')
