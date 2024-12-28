import calendar

while True:
    print("\n calender menu ")
    print("1. print specific month calendar")
    print("2. print specific year calendar")
    print("3. exit")
    choice = input ("enter the value")

    if choice == "1":
        y, m = int(input("Enter year: ")), int(input("Enter month (1-12): "))
        print(calendar.month(y, m))
    elif choice == "2":
        y = int(input("Enter year: "))
        print(calendar.calendar(y))
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
          