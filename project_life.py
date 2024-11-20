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