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


