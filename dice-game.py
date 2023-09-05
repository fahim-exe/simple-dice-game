import random as randi

def dice(amount:int):
   
    if amount<=0:
        raise ValueError
    rolls = [0]*amount

    for i in range(amount):
        r = randi.randint(1, 6)
        rolls[i] = r
    
    return rolls
    

def main():
    while True:
        try:
            user_input = input("How many dice you want to roll?")

            if user_input.lower()=="exit":
                print("Thanks for playing!!!")
                break
            
            print(dice(int(user_input)))
        except ValueError:
            print("Please enter a valid number!!!")
    


if __name__ == "__main__":
    main()