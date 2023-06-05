# Stock Price Guessing Game

A fun and interactive game where the player chooses a stock market stock by its ticker symbol and guesses if the stock price will go up or down.
The game fetches the current price of the stock using the Alpha Vantage API and compares the player's guess with the actual direction of the stock price.

## How to Play
1. Clone the repository or download the `stock_guessing_game.py` file.
2. Make sure you have Python 3 installed on your machine.
3. Install the `requests` library if it's not already installed. You can install it by running the following command:
    ```
    pip install requests
    ```
4. Obtain an API key from Alpha Vantage. You can sign up for a free API key at [Alpha Vantage API](https://www.alphavantage.co/).
5. Open the `stock_guessing_game.py` file in a text editor and replace `'YOUR_API_KEY'` with your actual Alpha Vantage API key in the `ALPHA_VANTAGE_API_KEY` variable.
6. Open a terminal or command prompt and navigate to the directory where the `stock_guessing_game.py` file is located.
7. Run the game by executing the following command:
    ```
    python stock_guessing_game.py
    ```
8. The game will display a welcome message and instructions on how to play. It will prompt you to enter the stock ticker symbol (e.g., AAPL, GOOGL, TSLA).
9. The game will fetch the current price of the stock using the Alpha Vantage API and present it to you. You need to guess if the stock price will go up or down.
10. The game will reveal the actual direction of the stock price, and if your guess matches, you win!
11. Enjoy playing the Stock Price Guessing Game and see if you can make accurate predictions!

## Dependencies
The game requires the following dependency:
- `requests`: A Python library for making HTTP requests. It can be installed using the following command:
    ```
    pip install requests
    or
    python -m pip install requests (from cmd)
    ```