# Negotiation Chatbot - README

## Overview

This project is a **Negotiation Chatbot** designed to handle price-based negotiations with users. It integrates **Gemini AI** to generate human-like, context-aware responses and **TextBlob** for real-time sentiment analysis, allowing the chatbot to dynamically adjust its replies based on the user's input and emotional tone. The chatbot engages in interactive conversations, generates counteroffers, and ensures a smooth negotiation process.

## Features

- **Dynamic Response Generation**: Uses Gemini AI to create tailored, polite responses based on user offers.
- **Sentiment Analysis**: Employs TextBlob to analyze user sentiment (positive, neutral, or negative) and adjust the chatbot’s responses accordingly.
- **Price Negotiation**: Extracts user-offered prices and provides counteroffers within an acceptable range.
- **Real-time Interaction**: Facilitates continuous conversation until an agreement is reached.

## Setup

1. Install dependencies:
   ```bash
   pip install google-generativeai textblob
   ```
2. Set your Gemini AI API key in the script:
   ```python
   api_key = "YOUR_API_KEY"
   ```

## Usage

Run the script and follow the prompts to negotiate:

```bash
python negotiation_chatbot.py
```

The chatbot will engage in a conversation, analyze the sentiment of the user's input, and offer appropriate responses based on price and tone.

## Conclusion

This project demonstrates how advanced AI and NLP tools can create interactive, intelligent systems for real-world applications like negotiation, providing a responsive and user-friendly experience.
