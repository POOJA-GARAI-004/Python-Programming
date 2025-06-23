import csv

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320
}

# Store user stock entries
portfolio = {}
total_investment = 0

print("=== Stock Portfolio Tracker ===")
print("Available stocks to track: ", ', '.join(stock_prices.keys()))

# Input stock data from user
while True:
    stock_symbol = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
    
    if stock_symbol == 'DONE':
        break

    if stock_symbol not in stock_prices:
        print("Stock not available. Please enter a valid stock symbol.")
        continue

    try:
        quantity = int(input(f"Enter number of shares for {stock_symbol}: "))
        if quantity < 0:
            print("Quantity cannot be negative.")
            continue
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if stock_symbol in portfolio:
        portfolio[stock_symbol] += quantity
    else:
        portfolio[stock_symbol] = quantity

    print(f"Recorded: {quantity} shares of {stock_symbol}")

# Calculate and display total investment
print("\n=== Portfolio Summary ===")
for symbol, qty in portfolio.items():
    price = stock_prices[symbol]
    value = price * qty
    total_investment += value
    print(f"{symbol}: {qty} shares × ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Save to text file
with open("portfolio_summary.txt", "w") as txt_file:
    txt_file.write("Stock Portfolio Summary\n")
    for symbol, qty in portfolio.items():
        price = stock_prices[symbol]
        value = price * qty
        txt_file.write(f"{symbol}: {qty} shares × ${price} = ${value}\n")
    txt_file.write(f"Total Investment: ${total_investment}\n")

# Save to CSV file
with open("portfolio_summary.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Stock Symbol", "Quantity", "Price per Share", "Total Value"])
    for symbol, qty in portfolio.items():
        price = stock_prices[symbol]
        value = price * qty
        writer.writerow([symbol, qty, price, value])
    writer.writerow(["", "", "Total Investment", total_investment])

print("\nPortfolio saved to 'portfolio_summary.txt' and 'portfolio_summary.csv'")
