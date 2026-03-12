import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

# Bulut adresimizi .env dosyasından çekiyoruz
MONGO_URI = os.getenv("MONGO_URI")

# Veritabanına bağlan
client = AsyncIOMotorClient(MONGO_URI)
database = client.error_tracker # Veritabanı adı
error_collection = database.get_collection("errors_history") # Tablo adı

# 1. FONKSİYON: Hataları Kaydetme
async def save_error_to_db(error_data: dict):
    try:
        await error_collection.insert_one(error_data)
        print("✅ Hata başarıyla MongoDB'ye kaydedildi!")
        return True
    except Exception as e:
        print(f"❌ DB Kayıt Hatası: {e}")
        return False

# 2. FONKSİYON: Hataları Okuma (Az önce eksik olan buydu!)
async def get_all_errors():
    try:
        # Veritabanındaki son 50 hatayı çekiyoruz (en yeniden eskiye)
        errors = await error_collection.find().sort("_id", -1).to_list(length=50)
        
        # MongoDB'nin özel ID formatını metne çeviriyoruz
        for err in errors:
            err["_id"] = str(err["_id"])
            
        return errors
    except Exception as e:
        print(f"❌ Veri Çekme Hatası: {e}")
        return []