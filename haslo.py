haslo_ok = False
while haslo_ok == False:
    password = input("Podaj nowe hasło: ")

    print(password)

    for letter in password:
        print(letter)
    
    has_lower = False
    has_upper = False
    is_digit = False
    Ilosc_znakow = len(password)
    print(Ilosc_znakow)

    Ile_duzych=0
    Ile_malych=0
    for char in password:  # idź znak po znaku
        if char.isalpha() and char.isupper():
            has_upper = True
            Ile_duzych += 1
            print('duze litery:',has_upper)
        if char.isalpha() and char.islower():
            has_lower = True
            Ile_malych += 1
        if char.isdigit():
            is_digit = True

    is_correct = has_lower and has_upper and is_digit and Ilosc_znakow >= 8
    if is_correct:
        print("Twoje hasło jest wystarczająco złożone")
        print("Ilosc dużych liter:", Ile_duzych)
        print("Ilosc małych liter:", Ile_malych)
        haslo_ok = True
    else:
        print("Zmien ponizsze rzeczy w Twoim hasle:")
        if not has_lower:
            print("- przynajmniej jedna mała litera")
        if not has_upper:
            print("- przynajmniej jedna duża litera")
        if not is_digit:
            print("-przynajmniej jedna cyfra")
        if Ilosc_znakow < 8:
            print("conajmniej 8 znaków")
