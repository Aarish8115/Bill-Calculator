from datetime import datetime # importing datetime

# total amount 
total = 0

# current date and time
now=datetime.now()

# display date and time format
date_=now.strftime("%d/%m/%Y %H:%M:%S")

# for starting the calculator
start=input("To start calculator press \"s\"\n")

# main while loop to start and end
while (start=="s"):

    # name of the recipient
    name=input("Enter recipient name \n")

    # for getting recipient number from atxt file
    with open("reciepts/reciept_no.txt") as f:
        recieptno=int(f.read())

    # for continuously asking the user for prices until he quits
    while (True):
        # to keep on asking the user for seperate items
        price=input("Enter item price or press q to quit\n")

        # if the user wants to quit
        if (price!="q"):
            # to add the prices
            total=total+int(price)
            # displaying the total amount
            print(f"Your total so far {total}")

        # to create a bill as a text file
        else:
            # creates the bill
            with open(f"reciepts/{recieptno}_{name}.txt","w") as i:
                i.write(f"Reciept No. {recieptno}\nName {name}\nTotal Rs.{total}\n{date_}")

            # to show the user his total
            print(f"Your total is {total}.\nThankyou for shopping with us.")

            # to edit the recipent number file so that it is ready for the next bill
            with open("reciepts/reciept_no.txt","w") as f:
                f.write(str(recieptno+1))

            # to get out of the while loop after everything is done
            break

    # again ask the user if he wants to use the calculator
    start = input("Enter s to start again\n")