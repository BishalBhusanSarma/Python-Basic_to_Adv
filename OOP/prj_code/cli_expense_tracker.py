import json
import time
file_name = "./expense.json"
with open(file_name, 'r') as file:
    expense = json.load(file)

while True:

    print("\nPress 1 to add expense")
    print("Press 2 to see expenses")
    print("Press 3 to see total expense")
    print("Press 4 to exit")


    choice = int(input("enter your choice: "))

    if(choice == 1):
        #input expenses
        amount = int(input("Amount is: "))
        reason = input("enter reason: ")

        exp = {'amount': amount,
               'reason':reason}
        expense.append(exp)

        with open(file_name, 'w') as file:
            json.dump(expense, file, indent=4)


        
    elif(choice == 2):
        #show expense & reason
        co = 1
        if(len(expense)==0):
            print("enter data")
        else:
            for e in expense:
                print(f"no. {co}: amount is {e['amount']} and reason is {e['reason']}")
                co +=1
    elif(choice == 3):

        #show total expenses

        total_exp = 0
        for te in expense:
            total_exp+=te['amount']
            
        print("total exp is ", total_exp)

    elif(choice == 4):
        #exit
        print("exiting...")
        time.sleep(2)
        break
    
    else:
        print("Invalid")