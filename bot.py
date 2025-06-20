# 1. Design the Chatbot’s Personality
BOT_NAME = "SlipCrypto"
BOT_TONE = "friendly and professional"

# 2. Predefined Crypto Data
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    },
    "Solana": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 7/10
    },
    "Polkadot": {
        "price_trend": "stable",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 9/10
    }
}

# Ethics Alert
DISCLAIMER = "Disclaimer: Cryptocurrency investments are highly volatile and risky. Always do your own thorough research before investing. This advice is for informational purposes only and not financial advice."

def get_recommendation(query):
    """
    Analyzes the user's query and provides a cryptocurrency recommendation
    based on predefined rules.
    """
    query = query.lower() # Convert query to lowercase for easier matching

    # 4. Add Advice Rules
    # Rule 1: Prioritize Sustainability
    if "sustainable" in query or "eco-friendly" in query or "green" in query:
        best_sustainable_coin = None
        max_sustainability = -1
        for coin, data in crypto_db.items():
            if data["sustainability_score"] > max_sustainability:
                max_sustainability = data["sustainability_score"]
                best_sustainable_coin = coin
        if best_sustainable_coin:
            return f"For sustainability and long-term potential, I recommend {best_sustainable_coin}! 🌱 It has a sustainability score of {crypto_db[best_sustainable_coin]['sustainability_score'] * 10}/10 and low energy use."
        else:
            return "I'm sorry, I couldn't find a strong recommendation based on sustainability right now."

    # Rule 2: Prioritize Profitability (Price Trend and Market Cap)
    elif "trending up" in query or "profitable" in query or "growth" in query or "buy" in query:
        top_profit_coins = []
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                top_profit_coins.append(coin)

        if top_profit_coins:
            return f"Looking for profitability? Coins like {', '.join(top_profit_coins)} are currently trending up with high market caps! 📈"
        else:
            # Fallback if no high market cap rising coins, suggest just rising ones
            rising_coins = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
            if rising_coins:
                return f"For potential growth, consider coins that are trending up, such as {', '.join(rising_coins)}. Remember, high market cap coins are generally more stable."
            else:
                return "Currently, I don't see any coins with a strong rising trend or high market cap in my data."

    # Rule 3: General "Best" or "Recommend" advice (combining both aspects implicitly)
    elif "best crypto" in query or "recommend" in query or "should I invest" in query:
        # A simple combined approach: prefer rising trend and high sustainability
        potential_buys = []
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] >= 7/10:
                potential_buys.append(coin)
            elif data["price_trend"] == "rising" and data["market_cap"] == "high":
                # Also consider high market cap and rising for general advice, even if sustainability isn't top
                potential_buys.append(coin)

        if potential_buys:
            # Remove duplicates if any
            potential_buys = list(set(potential_buys))
            return f"Based on both profitability and sustainability, you might consider {', '.join(potential_buys)}. They show good trends or strong eco-credentials! 🚀🌱"
        else:
            return "It's tricky to give a single 'best' recommendation without more specifics. What are you looking for most: profitability, sustainability, or something else?"

    # Fallback/Default Responses
    elif "hello" in query or "hi" in query or "hey" in query:
        return f"Hey there! I'm {BOT_NAME}. Let's find you a green and growing crypto! What can I help you with today?"
    elif "thank" in query or "bye" in query:
        return f"You're welcome! Happy to help. Remember {BOT_NAME} is always here for your crypto queries! Goodbye!"
    else:
        return "I'm not sure how to answer that. Could you rephrase your question or ask about profitability, sustainability, or general recommendations?"

def run_chatbot():
    """Starts and runs the CryptoBuddy chatbot interaction."""
    print(f"Hello! I'm {BOT_NAME}. Your {BOT_TONE} guide to the crypto world! ✨")
    print(DISCLAIMER)
    print("\nAsk me things like:")
    print("- 'Which crypto is trending up?'")
    print("- 'What's the most sustainable coin?'")
    print("- 'Which crypto should I buy for long-term growth?'")
    print("- 'What are some profitable coins?'")
    print("- 'Tell me about eco-friendly crypto.'")
    print("\nType 'exit' or 'quit' to end the chat.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print(f"{BOT_NAME}: Goodbye! Always do your own research! 🖖")
            break
        response = get_recommendation(user_input)
        print(f"{BOT_NAME}: {response}")
        print(DISCLAIMER) # Repeat disclaimer to reinforce the message

if __name__ == "__main__":
    run_chatbot()
