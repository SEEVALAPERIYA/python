while True:
    try:
        number1 = int(input('Number1: '))
    except ValueError:
        print("Not an integer! Please enter an integer.")
        continue
    else:
        break
