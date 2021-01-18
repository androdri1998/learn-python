phrase = input("Type a phrase: ")

amount_letter_a = phrase.count('a')
first_occurrence = phrase.index('a')
last_occurrence = phrase.rindex('a')

print("Amount letters 'a': {}".format(amount_letter_a))
print("First ocurrence letter 'a': {}".format(first_occurrence))
print("Last ocurrence letter 'a': {}".format(last_occurrence))
