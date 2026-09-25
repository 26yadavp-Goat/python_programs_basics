str1 = input("Enter a sentence: ")

words = str1.split()
longest_word = max(words, key=len)

print("Longest word:", longest_word)
print("Length:", len(longest_word))
