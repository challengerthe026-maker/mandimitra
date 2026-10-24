import google.generativeai as genai

# Setup AI 
genai.configure(api_key="AQ.Ab8RN6JW_HIMckxlY9IbsWyGe_4nVGBct8j5SioaIHt-0IwYAA")
model = genai.GenerativeModel('gemini-3.8-flash')

def get_mandi_advice(crop, location):
    prompt = f"""
    You are an expert agricultural market analyst in India. 
    A farmer wants to sell {crop} near {location}. 
    Provide a brief, helpful analysis in simple language:
    1. Realistic current price range per quintal in local mandis.
    2. Comparison with major regional hubs (like Vashi or Pune mandi).
    3. Actionable advice: Sell now or wait? Why?
    """
    response = model.generate_content(prompt)
    print("\n--- MANDI INSIGHTS ---")
    print(response.text)

# Quick Test
crop_input = input("Enter Crop Name (e.g., Onion, Wheat): ")
loc_input = input("Enter Your Location (e.g., Nashik, Pune): ")
get_mandi_advice(crop_input, loc_input)

# MandiMitra Testing

## Test 1: Mandi B gives a better return
•⁠  ⁠Quantity: 10 quintals
•⁠  ⁠Mandi A: ₹1800 per quintal
•⁠  ⁠Transport to A: ₹300
•⁠  ⁠Mandi B: ₹2100 per quintal
•⁠  ⁠Transport to B: ₹700

Expected:
•⁠  ⁠Mandi A net return: ₹17,700
•⁠  ⁠Mandi B net return: ₹20,300
•⁠  ⁠Better estimated return: Mandi B

## Test 2: Equal returns
Use values that produce the same net return at both mandis.
Expected: The app should report equal returns.

## Test 3: Invalid quantity
Enter zero or a negative quantity.
Expected: The app should ask for a valid quantity.

## Limitations
The prototype uses sample prices, not verified live mandi prices.
