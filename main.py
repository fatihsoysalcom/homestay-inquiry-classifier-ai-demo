import re

def classify_inquiry(inquiry_text):
    """
    Classifies a customer inquiry into predefined categories using keyword matching.
    This simulates a very basic 'AI' for automating customer service for Eden Homes.
    """
    inquiry_text = inquiry_text.lower()

    # Define keywords for different categories relevant to a homestay business
    categories = {
        "Reservation": ["book", "reserve", "stay", "room", "check-in", "check-out", "availability", "price", "cost", "night", "date"],
        "Amenities": ["wifi", "internet", "breakfast", "pool", "parking", "pet", "kitchen", "laundry", "air conditioning", "ac", "tv", "bathroom"],
        "Directions": ["how to get", "direction", "map", "location", "address", "find us", "airport", "station", "bus", "train"],
        "Feedback/Complaint": ["bad", "good", "experience", "problem", "issue", "happy", "unhappy", "review", "complain", "suggest"],
        "General Inquiry": [] # Catch-all for anything not specifically matched
    }

    scores = {cat: 0 for cat in categories}

    # Score based on keyword presence (demonstrates basic open-source AI logic)
    for category, keywords in categories.items():
        for keyword in keywords:
            # Use regex for whole word matching to avoid partial matches
            if re.search(r'\b' + re.escape(keyword) + r'\b', inquiry_text):
                scores[category] += 1

    # Determine the best category based on the highest score
    max_score = -1
    best_category = "General Inquiry" # Default if no specific keywords are found

    for category, score in scores.items():
        if score > max_score:
            max_score = score
            best_category = category
        elif score == max_score and category != "General Inquiry":
            # Simple tie-breaking: prefer specific categories over 'General Inquiry'
            # if scores are tied. If multiple specific categories tie, the first one encountered wins.
            pass

    # If no specific category scored, it's a general inquiry
    if max_score == 0 and best_category == "General Inquiry":
        return "General Inquiry"

    return best_category

def generate_response(category):
    """
    Generates a simple automated response based on the classified inquiry category.
    This shows how AI can automate initial customer interactions.
    """
    responses = {
        "Reservation": "Thank you for your reservation inquiry! Please visit our booking page at [Link to Booking Page] or call us at [Phone Number] to check availability and make a booking.",
        "Amenities": "We're happy to help with amenities questions! You can find a full list of our amenities on our website at [Link to Amenities Page]. Common amenities include Wi-Fi, breakfast, and free parking.",
        "Directions": "We'd love to welcome you! For detailed directions to Eden Homes, please visit [Link to Directions Page] or use the map on our contact page. Our address is [Your Address Here].",
        "Feedback/Complaint": "We appreciate your feedback! Please share more details with us directly at [Email Address] or call [Phone Number] so we can address your concerns promptly.",
        "General Inquiry": "Thank you for contacting Eden Homes! How can we assist you further? For common questions, please visit our FAQ at [Link to FAQ Page]."
    }
    return responses.get(category, "We received your inquiry. We'll get back to you shortly!")

def main():
    print("Welcome to Eden Homes AI Assistant (Open-Source Demo)!")
    print("This tool demonstrates how a simple AI can automate customer inquiry classification.")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("\nYour inquiry: ")
        if user_input.lower() == 'exit':
            break

        # Simulate AI processing for inquiry classification
        category = classify_inquiry(user_input)
        # Generate an automated response based on the classification
        response = generate_response(category)

        print(f"\nAI classified this as: '{category}'") # Illustrates the AI's classification output
        print(f"Suggested automated response: {response}") # Shows the automated action/response
        print("\n---")

if __name__ == "__main__":
    main()
