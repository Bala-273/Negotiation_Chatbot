import google.generativeai as genai
from textblob import TextBlob
import os

# Configure the Gemini AI API key
api_key = "API_KEY"
genai.configure(api_key=api_key)

# Define price limits for negotiation
min_price = 1000
max_price = 4000

# Function to call Gemini AI model for response generation
def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-pro")
    chat = model.start_chat(history=[])
    
    response = chat.send_message(prompt)
    
    # Combine the response into a single string
    generated_text = ''.join([chunk.text for chunk in response])
    return generated_text

# Function to negotiate based on user input
def negotiate(user_input):
    # Analyze sentiment of the user input
    sentiment = analyze_sentiment(user_input)

    # Extract price from user input
    user_price = extract_price(user_input)

    # Negotiate based on the price
    if user_price is not None:
        if is_offer_acceptable(user_price):
            if sentiment > 0:
                # Positive sentiment: Offer a better deal
                generated_text = f"That's a great offer! Here's a 10% discount, making it ${user_price * 0.9:.2f} We have a deal!"
            else:
                # Neutral/Negative sentiment: Accept offer
                generated_text = f"I'm happy to accept your offer of ${user_price}. We have a deal!"
            return generated_text, True  # Return with a flag to end the loop
        else:
            # Generate a counteroffer using the Gemini model
            prompt = f"The user offered {user_price}. The acceptable range is between {min_price} and {max_price}. Generate a polite counteroffer."
            generated_text = get_gemini_response(prompt)
            return generated_text, False  # Continue the negotiation
    else:
        return "Sorry, I couldn't understand the price you mentioned. Can you please clarify?", False

# Function to check if the offer is acceptable
def is_offer_acceptable(user_price):
    return min_price <= user_price <= max_price

# Function to extract price from user input using basic NLP
def extract_price(text):
    words = text.split()
    for word in words:
        try:
            price = int(word)
            return price
        except ValueError:
            continue
    return None

# Function to analyze the sentiment of the user input
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment

# Main loop for user interaction
if __name__ == "__main__":
    while True:
        user_input = input("Enter your offer: ")
        response, negotiation_done = negotiate(user_input)
        print(response)

        if negotiation_done:
            print("Negotiation complete. Thank you!")
            break  # Exit the loop after a deal is made
