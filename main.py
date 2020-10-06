from datetime import date
# Ask user name and age
name = input("Hogy hívnak: ")
age = int(input("Mond meg hány éves vagy: "))
szaz = 100-age
# Print a msg w/ their name and tell when they turn a 100yrs old
today = date.today()
hundred = today.year + szaz
String = "Szia " + name + " ma " + str(age) + " éves vagy. Azaz " + str(szaz) + " év múlva leszel 100 éves " + str(hundred) + " ben.\n"
print(String)
# Extra: Ask a user input and multiply the previous print statement btw (1-10)
n = int(input("Kérek egy számot 1-10 között: "))
print(String*n)
