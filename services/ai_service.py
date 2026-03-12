import google.generativeai as genai
import os

def analyze_error_with_ai(message: str, stack: str):
    # API key'i .env dosyasından alacağız
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Hata: {message}\nStack: {stack}\nNeden oldu ve nasıl çözülür?"
    response = model.generate_content(prompt)
    return response.text