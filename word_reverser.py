text = input("Enter a sentence: ")

words = text.split()
reversed_text = " ".join(reversed(words))

print("\nReversed sentence:")
print(reversed_text)
