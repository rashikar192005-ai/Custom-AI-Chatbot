from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("==============================================")
print("   Automated Copywriting & Tone Transformer")
print("==============================================")

# Get user inputs
product_name = input("Enter Product Name: ")
platform = input("Enter Platform (LinkedIn/Instagram/Email): ")
tone = input("Enter Tone (Professional/Friendly/Exciting): ")
description = input("Enter Product Description: ")

# Get model parameters
temperature = float(input("Enter Temperature (0.0 - 1.0): "))
top_p = float(input("Enter Top_P (0.0 - 1.0): "))

# Dynamic prompt template
prompt = f"""
Create professional marketing copy for the following product.

Product Name: {product_name}
Platform: {platform}
Tone: {tone}
Product Description: {description}

Instructions:
- Write content specifically for the selected platform.
- Follow the requested tone.
- Make the content clear, engaging and professional.
- Use only the information provided in the product description.
- Do not invent important product features.
"""

print("\nGenerating marketing copy...\n")

try:

    response = client.chat.completions.create(
        model="gpt-5.6-luna",

        messages=[
            {
                "role": "system",
                "content": "You are a professional marketing copywriter."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=temperature,
        top_p=top_p
    )

    result = response.choices[0].message.content

    print("==============================================")
    print("             GENERATED MARKETING COPY")
    print("==============================================")
    print(result)
    print("==============================================")

except Exception as e:

    print("==============================================")
    print("                ERROR")
    print("==============================================")
    print(e)
    print("==============================================")