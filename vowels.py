# Write a program to check if a character is a vowel or consonant.

char = input("enter any alpahbate: ")

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

if char in vowels:
    print("the alphabet is a vowel.")

else:
    print("the alphabate is a consonant")    