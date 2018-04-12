# the following code is a "shell" for COMP 151 assognment #5

#getCoins: accepts a list of random quarters, dimes, nickels and pennies expressed in cents; returns the total in pennies
def getCoins():
    total=0
    #input a list of coins from the keyboard
    coinList=eval(input("Enter list of coins : "))
    #add up the coins
    for coin in coinList:
        total += coin
    #return total pennies
    return total

#calcChange: convert an amount in pennies into a count of the number of dollars, quarters, dimes, nickels and pennies
#Return the result in the form of a list
def calcChange(amount):
    changeList=[0,0,0,0,0]
    #calculate # of dollars
    changeList[0]=amount//100
    #calculate remining pennies
    amount=amount%100
    # calculate # of quarters
    changeList[1] = amount // 25
    # calculate remining pennies
    amount = amount % 25
    # calculate # of dimes
    changeList[2] = amount // 10
    # calculate remining pennies
    amount = amount % 10
    # calculate # of nickels
    changeList[3] = amount // 5
    # calculate remining pennies
    amount = amount % 5
    # calculate # of pennies
    changeList[4] = amount
    #return the list of coins
    return changeList

def main():
    # list of items for sale
    itemList = [["Candy", 125], ["Water", 75], ["Granola Bar", 100]]
    print("Select from the following choices:")
    print("Select 0 for Candy price: 1.25")
    print("Select 1 for Water price: 0.75")
    print("Select 2 for Granola Bar price: 1.0")
    totalInput = getCoins()
    print("Total is $", totalInput/100)
    while True:
        # Do while != 9
        # Make sure cost is less than or equal to totalInput
        # Handle cases where they select items that do not exis
        choice = eval(input("Enter selection or 9 to get change"))
        if(choice == 9):
            break
        if(totalInput <= itemList[choice][1]):
            print("Not Enough Dough, Boy")
        else:
            print("Vending",itemList[choice][0])
            totalInput -= itemList[choice][1]
            print("total remaining is $",totalInput/100)
            change = calcChange(totalInput)

    print("Dispencing Change $",totalInput/100)
    print(change[0],"Dollars")
    print(change[1],"Quarters")
    print(change[2],"Dimes")
    print(change[3],"Nickles")
    print(change[4],"Pennies")

main()