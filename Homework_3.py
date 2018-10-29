sender = "Paula"
blockchain = [["0", ["genesis", 0, "genesis"]]]

# nueva transaccion, la determinacion de la definicon será contada por
# las tabulaciones; elementos externos a la tabulaciion 2 estan fuera#

def new_transaction():
    amount = int(input("Give me the amount! "))
    recipient = input("Where to send it to? ")
    blockchain.append([blockchain[-1][1], [sender, amount, recipient]])


def output_blockchain():
    print(blockchain)

def check_blockchain():
    for position in range(1, len(blockchain)):
        if blockchain[position - 1][1] == blockchain[position][0]:
            continue
        else:
            return False
    return True

def manipulate_chain():
    output_blockchain()
    position = int(input("Whach block is it in miin! "))
    position_2 = int(input("Whst daaaata bro wanna change? "))
    update_data = input("To what amigo? ")
    if position_2 == 1:
        update_data = int(update_data)
    blockchain[position][1][position_2] = update_data

def main_menu():
    choice = ""
    while choice != "q":
        print("1: Add a new transaction")
        print("2: Output the blockchain blocks")
        print("h: Manipulate the chain")
        print("q: Quit")
        choice = input("What chu wanna do bitsch! ")

        if choice == "1":
            new_transaction()
        elif choice == "2":
            output_blockchain()
        elif choice == "h":
            manipulate_chain()

main_menu()