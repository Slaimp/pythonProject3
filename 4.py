class CryptoExchange:
    total_transactions = 0
    total_exchanges = 0

    def __init__(self, name, available_bitcoin, available_ethereum):
        self.name = name
        self.available_bitcoin = available_bitcoin
        self.available_ethereum = available_ethereum
        CryptoExchange.total_exchanges += 1

    def buy_crypto(self, crypto_type, quantity, price):
        if crypto_type.lower() == "bitcoin" and quantity <= self.available_bitcoin:
            cost = quantity * price
            print(f"Buying {quantity} Bitcoin for {cost} USD at {self.name}")
            self.available_bitcoin -= quantity
            CryptoExchange.total_transactions += 1
        elif crypto_type.lower() == "ethereum" and quantity <= self.available_ethereum:
            cost = quantity * price
            print(f"Buying {quantity} Ethereum for {cost} USD at {self.name}")
            self.available_ethereum -= quantity
            CryptoExchange.total_transactions += 1
        else:
            print(f"Sorry, not enough {crypto_type} in stock at {self.name}")

    def sell_crypto(self, crypto_type, quantity, price):
        if crypto_type.lower() == "bitcoin" and quantity <= self.available_bitcoin:
            earnings = quantity * price
            print(f"Selling {quantity} Bitcoin for {earnings} USD at {self.name}")
            self.available_bitcoin += quantity
            CryptoExchange.total_transactions += 1
        elif crypto_type.lower() == "ethereum" and quantity <= self.available_ethereum:
            earnings = quantity * price
            print(f"Selling {quantity} Ethereum for {earnings} USD at {self.name}")
            self.available_ethereum += quantity
            CryptoExchange.total_transactions += 1
        else:
            print(f"Sorry, not enough {crypto_type} in stock at {self.name}")

    @staticmethod
    def show_total_transactions():
        print(f"Total transactions across all crypto exchanges: {CryptoExchange.total_transactions}")

    @classmethod
    def show_total_exchanges(cls):
        print(f"Total number of crypto exchanges: {cls.total_exchanges}")


exchange_name = input("Enter the name of the crypto exchange: ")
bitcoin_stock = float(input("Enter the available quantity of Bitcoin: "))
ethereum_stock = float(input("Enter the available quantity of Ethereum: "))

crypto_exchange = CryptoExchange(exchange_name, bitcoin_stock, ethereum_stock)

crypto_type = input("Enter the type of cryptocurrency (Bitcoin/Ethereum): ")
transaction_type = input("Enter the transaction type (Buy/Sell): ")
quantity = float(input("Enter the quantity of cryptocurrency: "))
price = float(input("Enter the price per unit: "))

if transaction_type.lower() == "buy":
    crypto_exchange.buy_crypto(crypto_type, quantity, price)
elif transaction_type.lower() == "sell":
    crypto_exchange.sell_crypto(crypto_type, quantity, price)

CryptoExchange.show_total_transactions()
CryptoExchange.show_total_exchanges()
