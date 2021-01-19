phrase = str(input("Type a phrase: ")).strip()

amount_letter_a = phrase.lower().count('a')
first_occurrence = phrase.lower().index('a')
last_occurrence = phrase.lower().rindex('a')

print("Amount letters 'a': {}".format(amount_letter_a))
print("First ocurrence letter 'a': {}".format(first_occurrence))
print("Last ocurrence letter 'a': {}".format(last_occurrence))
