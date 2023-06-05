import random
import requests

ALPHA_VANTAGE_API_KEY = 'YOUR_API_KEY'

def get_stock_price(ticker):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    data = response.json()
    if 'Global Quote' in data:
        return float(data['Global Quote']['05. price'])
    else:
        return None

def play_game():
    print("Welcome to the Stock Price Guessing Game!")
    print("-----------------------------------------")
    print("Choose a stock by its ticker symbol and guess if the stock price will go up or down.")
    print("I will give you the current stock price, and you have to make your prediction.")
    print("-----------------------------------------")
    
    ticker = input("Enter the stock ticker symbol (e.g., AAPL, GOOGL, TSLA): ")
    stock_price = get_stock_price(ticker)
    
    if stock_price is None:
        print("Error: Failed to fetch the stock price. Please try again.")
        return
    
    print(f"The current price of {ticker} is ${stock_price:.2f}")
    
    direction = random.choice(["up", "down"])
    guess = input("Will the stock price go up or down? Enter 'up' or 'down': ")
    
    if guess.lower() == direction:
        print("Congratulations! You guessed correctly!")
    else:
        print("Oops! You guessed incorrectly.")
    
    print(f"The stock price was predicted to go {direction}.")
    print("-----------------------------------------")

play_game()
