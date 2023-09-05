import random as randi

def dice(amount:int):
    sum = 0
   
    if amount<=0:
        raise ValueError
    rolls = [0]*amount

    for i in range(amount):
        r = randi.randint(1, 6)
        rolls[i] = r
        sum = sum+r
    
    return rolls
    

def main():
    while True:
        try:
            print()
            user_input = input("How many dice you want to roll?")

            if user_input.lower()=="exit":
                print("Thanks for playing!!!")
                break
            d = dice(int(user_input))
            s = sum(d)
            print()
            print(*d, sep=", ")
            print("Total sum of dices:", s)
            print()
            
        except ValueError:
            print("Please enter a valid number!!!")
    


if __name__ == "__main__":
    main()