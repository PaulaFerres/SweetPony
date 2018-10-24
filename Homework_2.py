sender = "Paula"
blockchain = []


amount = int(input("Give me the amount! "))
recipient = input("Where to send it to? ")
blockchain.append([sender, amount, recipient])

transaction = []
amount = int(input("Give me the amount! "))
recipient = input("Where to send it to? ")
transaction.append(sender)
transaction.append(amount)
transaction.append(recipient)
blockchain.append(transaction)

transaction = []
amount = int(input("Give me the amount! "))
recipient = input("Where to send it to? ")
transaction.append(sender)
transaction.append(amount)
transaction.append(recipient)
blockchain.append(transaction)

print(blockchain)