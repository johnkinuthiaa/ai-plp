# SlipCrypto Chatbot

## A Rule-Based Cryptocurrency Investment Advisor

**SlipCrypto** is a simple, rule-based chatbot designed to provide introductory investment advice on cryptocurrencies, focusing on both profitability trends and sustainability aspects. It leverages predefined data to respond to user queries about crypto assets.

### Features

* **Personality:** Friendly and professional tone from "SlipCrypto".

* **Profitability Analysis:** Recommends coins based on "rising" price trends and "high" market capitalization.

* **Sustainability Focus:** Highlights eco-friendly cryptocurrencies with "low" energy usage and high "sustainability scores".

* **General Advice:** Provides combined recommendations based on both profitability and sustainability.

* **Clear Disclaimer:** Constantly reminds users about the risks of crypto investments and the importance of personal research.

### How to Run

1.  **Save the code:** Save the provided Python code as a `.py` file (e.g., `bot.py`).

2.  **Open a terminal:** Navigate to the directory where you saved the file.

3.  **Run the script:** Execute the script using the Python interpreter:

    ```
    python bot.py


    ```

### Sample Data

The bot uses the following internal dataset:


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


### Example Interactions

You can ask SlipCrypto questions like:

* "Which crypto is trending up?"

* "What's the most sustainable coin?"

* "Which crypto should I buy for long-term growth?"

* "What are some profitable coins?"

* "Tell me about eco-friendly crypto."

* "Hello" / "Hi"

* "Thank you" / "Bye"

**Example Conversation:**


You: Which crypto should I buy for long-term growth?
SlipCrypto: Based on both profitability and sustainability, you might consider Bitcoin, Cardano, Solana. They show good trends or strong eco-credentials! 🚀🌱
Disclaimer: Cryptocurrency investments are highly volatile and risky. Always do your own thorough research before investing. This advice is for informational purposes only and not financial advice.

You: What's the most sustainable coin?
SlipCrypto: For sustainability and long-term potential, I recommend Polkadot! 🌱 It has a sustainability score of 9.0/10 and low energy use.
Disclaimer: Cryptocurrency investments are highly volatile and risky. Always do your own thorough research before investing. This advice is for informational purposes only and not financial advice.


### Ethics Alert & Disclaimer

**IMPORTANT:** Cryptocurrency investments are highly volatile and risky. Always do your own thorough research before investing. The advice provided by SlipCrypto is for informational purposes only and should **not** be considered financial advice.

