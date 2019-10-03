def menu():
    print("************MAIN MENU**************")
    # time.sleep(1)
    print()

    choice = input("""
                      A: Enter Student details
                      B: View Student details
                      C: Search by ID number
                      D: Produce Reports
                      Q: Quit/Log Out

                      Please enter your choice: """)

    if choice == "A" or choice == "a":
        pass
    elif choice == "B" or choice == "b":
        pass
    elif choice == "C" or choice == "c":
        pass
    elif choice == "D" or choice == "d":
        pass
    elif choice == "Q" or choice == "q":
        pass
    else:
        print("You must only select either A,B,C, or D.")
        print("Please try again")
        menu()


menu()