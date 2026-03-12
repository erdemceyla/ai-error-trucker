import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
from google import genai
from database import save_error_to_db, get_all_errors # Veritabanı fonksiyonları eklendi

load_dotenv()

# AI İstemci Yapılandırması
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI(title="AI Error Tracker")

# CORS Ayarları (Frontend'in Backend ile konuşabilmesi için)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ErrorLog(BaseModel):
    source: str
    message: str
    stack: Optional[str] = "Stack trace yok."

@app.post("/log-error")
async def collect_error(error: ErrorLog):
    # Varsayılan mesaj (AI kotaya takılırsa bu kaydedilecek)
    ai_result = "AI Analizi şu an yapılamıyor (Kota veya bağlantı sorunu)."
    
    # 1. ADIM: Yapay Zeka Analizi
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"Sen bir yazılım uzmanısın. Şu hatayı analiz et ve çözüm sun:\n{error.message}"
        )
        ai_result = response.text
    except Exception as e:
        print(f"⚠️ AI API Hatası Yakalandı (Sistem çalışmaya devam ediyor): {e}")

    # 2. ADIM: Veritabanına Kayıt (AI çökse bile çalışır)
    try:
        error_record = {
            "source": error.source,
            "message": error.message,
            "stack": error.stack,
            "ai_analysis": ai_result
        }
        await save_error_to_db(error_record)
    except Exception as db_err:
        print(f"❌ Veritabanı Hatası: {db_err}")

    # 3. ADIM: Sonucu Test Sayfasına Gönder
    return {"ai_analysis": ai_result}

# 🌟 YÖNETİM PANELİ İÇİN EKLENEN ROTA BURASI 🌟
@app.get("/api/errors")
async def fetch_errors():
    errors = await get_all_errors()
    return {"status": "success", "data": errors}

@app.get("/")
def home():
    return {"message": "AI Error Tracker API Çalışıyor!"}