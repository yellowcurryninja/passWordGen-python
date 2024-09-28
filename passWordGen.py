import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'fetchLetters', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
print("Password Generator")
nr_letters = int(input("how many letters would you like in your password?\n"))
nr_symbols = int(input(f"how many symbols would you like?\n"))
nr_numbers = int(input(f"how many numbers would you like?\n"))
fetchLetters = random.choices(letters, k=nr_letters)
x = ""
for i in fetchLetters:
    x += i
    password.append(i)
y = ""
fetchSymbols = random.choices(symbols, k=nr_symbols)
for signs in fetchSymbols:
    y +=signs
    password.append(signs)
z =""
fetchNumbers = random.choices(numbers, k=nr_numbers)
for digits in fetchNumbers:
    z += str(digits)
    password.append(digits)
random.shuffle(password)
finalResult = ""
for new in password:
    finalResult += new
print(finalResult)