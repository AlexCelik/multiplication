def multiplication():
    choice = int(input())
    multiple = 1

    while multiple < 11:
        total = choice * multiple
        multiple += 1
        print(total)

    restart = int(input("Restart ? [1 for yes] [2 for no] \n"))
    if restart == 1:
        multiplication()
    else:
        print ("salut")

multiplication()













