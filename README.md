```python


F = int(input("Įveskite temperatūrą pagal Farenheitą: "))

C = (F-32) * 5 / 9

print (f"Temperatura pagal Celsiju: {C} ")


name = input ("Iveskite zodi: ")

print (f"Apverstas zodis: {name[::-1]}")


name = input ("Iveskite savo varda: ")

surname = input ("Iveskite savo pavarde: ")

print (f"Formuotas vardas: {surname}, {name}")


P = float(input("Iveskite pradine suma: "))
N = float(input("Iveskite palukanu norma (%): "))
L = float(input("Iveskite laika (metais): "))
PP = (P * N * L) / 100

print (f"Paprastosios palukanos yra {PP}")


full_name = input ("Iveskite savo pilna varda: ")

first_name = full_name.split()[0]

greeting = "Labas, " + first_name.upper() + ", sveiki atvyke!"

print (greeting)


numb1 = float(input("Iveskite pirma skaiciu: "))

numb2 = float(input("Iveskite antra skaiciu: "))

if numb1 < numb2:
    print (f"Didesnis skaicius yra {numb2} ")
elif numb1 > numb2:
    print (f"Didesnis skaicius yra {numb1} ")
elif numb1 == numb2:
    print ("Skaiciai yra lygus")


name = input("Iveskite savo varda: ")
surname = input("Iveskite savo pavarde: ")
age = int(input("Iveskite savo amziu: "))

if age >= 21:
    print (f" {name} {surname}, jus galite patekti i kazino")
elif age < 21:
    print (f" {name} {surname}, jus negalite patekti i kazino")


numb1 = float(input("Iveskite pirma skaiciu: "))
symbol = input ("Iveskite simboli: ")
numb2 = float(input("Iveskite antra skaiciu: "))

result = None

if symbol == "+":
    result = numb1 + numb2
elif symbol == "-":
    result = numb1 - numb2
elif symbol == "*":
    result = numb1 * numb2
elif symbol == "/":
    result = numb1 / numb2

print (f"{numb1} {symbol} {numb2} rezultatas yra {result}")


member = input ("Ar esate bibliotekos narys? (taip / ne): ").lower()

if member == "taip":
    age = int(input("Iveskite savo amziu: "))
    if age >= 12:
        print ("Jus galite skolintis visas knygas")
    else:
        adult = input("Ar jus lydi suauges asmuo? (taip/ne): ").lower()
        if adult == "taip":
            print("Jus galite skolintis visas knygas")
        else:
            print("Jus galite skolintis tik vaiku knygas")

else:
    print ("Jus negalite skolintis jokiu knygu")

# Loops tasks

number1 = int(input("Iveskite sveikaji skaiciu 1: "))
number2 = int(input("Iveskite sveikaji skaiciu 2: "))
number3 = int(input("Iveskite sveikaji skaiciu 3: "))
number4 = int(input("Iveskite sveikaji skaiciu 4: "))
number5 = int(input("Iveskite sveikaji skaiciu 5: "))
number6 = int(input("Iveskite sveikaji skaiciu 6: "))
number7 = int(input("Iveskite sveikaji skaiciu 7: "))
number8 = int(input("Iveskite sveikaji skaiciu 8: "))
number9 = int(input("Iveskite sveikaji skaiciu 9: "))
number10 = int(input("Iveskite sveikaji skaiciu 10: "))

suma = (number1 + number2 + number3 + number4 + number5 + number6 + number7 + number8 + number9+ number10)
average = (number1 + number2 + number3 + number4 + number5 + number6 + number7 + number8 + number9+ number10) / 10
print (f"Suma: {suma}, Vidurkis: {average} ")


total_sum = 0

for i in range (10):
    number = int(input(f"Iveskite sveikaji skaiciu {i + 1}: "))
    total_sum += number

average = total_sum / 10
print (f"Suma: {total_sum}, Vidurkis: {average}")

while True:
    name = input("Iveskite vartotojo varda: ")
    password = input("Iveskite slaptazodi: ")
    if name == "user123" and password == "securepass":
        print (f"Prisijungimas sekmingas! Sveiki,{name}. ")
        break

while True:
    PIN = int(input( "Iveskite PIN koda: "))
    if PIN == 1234:
        print (f"Surastas PIN: {PIN}")
        break

stored_pin = "1234"

for i in range (10000):
    pin = str(i).zfill (4)
    if pin == stored_pin:
        print (f"Surastas PIN: {pin}")
        break

a = 0
b = 1

print (f"Fibonacci seka:", end = "")
print (a, b, end = "")

for i in range (8):
    a, b = b, a + b
    print (b, end = "")



numbers = []

while True:
    entry = input("Iveskite skaiciu (arba iveskite 'pabaiga'): ")
    if entry == ("pabaiga"):
        break
    numbers.append(float(entry))

average = sum(numbers) / len(numbers) if numbers else 0

print(f"Skaičiai: {numbers}")
print(f"Vidurkis: {average}")

# Sarasai ir tuples

shopping_list = ["pienas", "kiausiniai", "duona", "sviestas"]

print (shopping_list)
print (shopping_list[0])

shopping_list.insert(2, "bananas")
shopping_list.remove("duona")
print (shopping_list)

shopping_list.insert(0, "obuolys")

print (shopping_list)

shopping_list.append ("miltai")
shopping_list.append ("cukrus")

print (shopping_list)

print (shopping_list[2:4])


day_temperatures = (22.6, 19.1, 21.3)
number_elements = len(day_temperatures)
print (number_elements)



size = int(input("Iveskite trikampio dydi: "))

for i in range(1, size + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()



start = int(input("Iveskite intervalo pradzia:"))
end = int(input("Iveskite intervalo pabaiga:"))

primes = []

for num in range(start, end + 1):
    if num > 1:
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

print("Pirminiai skaičiai:", primes)

# Dictionaries and sets

user_info = {"vardas": input("Irasykite savo varda: "),
             "pavarde": input ("Irasykite savo pavarde: "),
             "amzius": int(input("Irasykite savo amziu: "))}
print (user_info)


students = set()

while True:
    student = input("Įveskite mokinio vardą (arba įveskite 'pabaiga') ")
    if student.lower() == "pabaiga":
        break
    students.add(student)
    print(f"{student} pridėta prie sąrašo.")

print("Mokinių, kurie vyksta į kelionę, sąrašas:", students)



dictionary = {
    "obuolys": "vaisius, augantis ant medžių",
    "knyga": "rinkinys atspausdintų lapų, susegtų kartu, turintis tekstą ar paveikslėlius",
    "kompiuteris": "elektroninis įrenginys, skirtas duomenims saugoti ir apdoroti",
}

while True:
    word = input("Iveskite zodi, kad suzinotumete jo reiksme (arba 'pabaiga'): ")
    if word.lower() == "pabaiga":
        break
    if word in dictionary:
        print(f"Žodžio {word} reikšmė: {dictionary[word]}.")
    else:
        print ("Sio zodzio musu zodyne nera")



contacts = {}

while True:
    action = input("Pasirinkite veiksmą: Prideti, Ieskoti, Istrinti arba Iseiti: ").lower()
    if action == "prideti":
        name = input("Iveskite varda:")
        number = input ("Iveskite telefono numeri: ")
        contacts[name] = number
        print("Kontaktas pridėtas.")
    elif action == "ieskoti":
        name = input("Įveskite kontakto vardą paieškai: ")
        print(f"Telefono numeris: {contacts.get(name, 'Nerasta')}")
    elif action == "istrinti":
        name = input("Iveskite kontakto varda, kuri noretumete istrinti: ")
        if name in contacts:
            del contacts[name]
            print("Kontaktas ištrintas.")
        else:
            print("Kontaktas nerastas.")
    elif action == "iseiti":
        print("Išeinama iš telefono knygos.")
        break
    else:
        print("Netinkamas veiksmas. Prašome pasirinkti iš naujo.")

    print("Visi kontaktai:", contacts)

# iki cia ikelta i Github

# functions

def is_even_or_odd(num):
    if num == 0:
        return "Neither"
    if num % 2 == 0: # ar lyginis ar nelyginis
        return "Even"
    else:
        return "Odd"

print (f"5 is {is_even_or_odd(5)}")
print (f"12 is {is_even_or_odd(12)}")
print (f"100 is {is_even_or_odd(100)}")
print (f"0 is {is_even_or_odd(0)}")
is_even_or_odd(5)


def simple_calculator (a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b

print (simple_calculator(5, 8, "add"))
print (simple_calculator(1, 9, "multiply"))
print (simple_calculator(100, 100, "subtract"))



def calculate_bmi(height, weight):
    return weight / (height**2)

height = float(input("Įveskite ūgį metrais: "))
weight = float(input("Įveskite svorį kilogramais: "))
bmi = calculate_bmi(height, weight)
print(f"KMI yra {bmi:.2f}.")



def validate_email(email):
    if email.count("@") != 1:
        return False
    username, domain = email.split("@")
    if not username:
        return False
    if "." not in domain:
        return False
    domain_parts = domain.split(".")
    if any(len(part) == 0 for part in domain_parts[:-1]):
        return False
    # Patikriname, ar domeno galūnė yra bent 2 simbolių ilgio
    if len(domain_parts[-1]) < 2:
        return False
    return True


email = input("Įveskite el. pašto adresą: ")
if validate_email(email):
    print("El. pašto adresas galiojantis.")
else:
    print("El. pašto adresas negaliojantis.")


