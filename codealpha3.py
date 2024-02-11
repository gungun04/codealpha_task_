import yfinance as yf

class Stock:
    def __init__(self,symbol,shares):
        self.symbol = symbol
        self.shares = shares
        self.update_data()

    def update_data(self):
        self.data = yf.download(self.symbol,start="2022-01-01", end="2024-01-01")

    def calculate_value(self):
        return self.shares * self.data['close'].iloc[-1]
    
class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self,stock):
        self.stocks.append(stock)
        stock.update_data()

    def remove_stock(self,symbol):
        self.stocks = [stock for stock in self.stocks if stock.symbol != symbol]

    def calculate_total_value(self):
        total_value = sum(stock.calculate_value() for stock in self.stocks)
        return total_value
    
if __name__ == "__main__":
        portfolio = Portfolio()

        while True:
            print("\n1.Add Stock\n2. Remove Stock\n3. Track Portfolio\n4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                symbol = input("Enter stock symbol1: ")
                shares = float(input("Enter the number of shares: "))
                stock = Stock(symbol,shares)
                portfolio.add_stock(stock)
                print(f"{symbol} added to the portfolio.")

            elif choice == '2':
                symbol_to_remove = input("Enter stock symbol to remove: ")
                portfolio.remove_stock(symbol_to_remove)
                print(f"{symbol_to_remove} removed from the portfolio.")

            elif choice == '3':
                total_portfolio_value = portfolio.calculate_total_value()
                print(f"\nTotal Portfolio Value: ${total_portfolio_value:.2f}")

                for stock in portfolio.stocks:
                    print(f"{stock.symbol}: {stock.shares} shares | Current Value: ${stock.calculate_valu():.2f}")

            elif choice == '4':
                print("Exiting the portfolio tracker.")
                break

            else:
                print("Invalid choice. Please try again.")
