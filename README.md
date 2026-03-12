# 🚀 AI Destekli Full-Stack Hata Takip Sistemi (Error Tracker)

Bu proje; Frontend tarafında oluşan hataları anında yakalayan, FastAPI ile oluşturulmuş Backend'e ileten ve **Google Gemini AI** kullanarak bu hataları analiz edip çözüm önerileri sunan tam teşekküllü bir hata yönetim sistemidir. 

Ayrıca sistemin "Fault-Tolerant" (hata tolere edebilir) yapısı sayesinde, dış AI servislerinde kota dolumu veya çökme yaşansa dahi sistem çalışmaya devam eder ve hataları bulut tabanlı **MongoDB Atlas** veritabanına güvenle kaydeder.

## 🛠️ Kullanılan Teknolojiler

* **Backend:** Python, FastAPI, Uvicorn
* **Yapay Zeka:** Google GenAI SDK (Gemini 2.0 Flash / 1.5 Flash 8B)
* **Veritabanı:** MongoDB Atlas (Bulut), Motor (Asenkron sürücü)
* **Frontend:** HTML5, Vanilla JavaScript, Fetch API

## ✨ Öne Çıkan Özellikler

* **Gerçek Zamanlı Hata Yakalama:** Tarayıcıda oluşan hatalar anında API'ye iletilir.
* **Yapay Zeka ile Kod Analizi:** Gemini AI, hatanın nedenini ve olası çözüm yollarını açıklar.
* **Zarif Çöküş (Graceful Degradation):** AI kotası dolsa veya servis yanıt vermese bile, hata kayıt süreci kesintiye uğramaz ve veritabanına yazılır.
* **Asenkron Mimari:** Veritabanı ve AI istekleri asenkron (`async/await`) olarak yönetilir.
* **Yönetim Paneli (Dashboard):** Veritabanına kaydedilen hatalar ve AI analizleri özel bir arayüzde şık kartlar halinde listelenir.

## ⚙️ Nasıl Çalıştırılır?

1. Projeyi klonlayın: `git clone https://github.com/erdemceyla/ai-error-trucker.git`
2. Gerekli kütüphaneleri kurun: `pip install fastapi uvicorn pydantic python-dotenv google-genai motor dnspython`
3. Proje dizininde bir `.env` dosyası oluşturun ve içine şu bilgileri ekleyin:
   ```env
   GEMINI_API_KEY=sizin_api_anahtariniz
   MONGO_URI=sizin_mongodb_baglanti_linkiniz
4. Backend sunucusunu başlatın: uvicorn main:app --reload
5. Test için hata_test.html dosyasını, hataları görüntülemek için dashboard.html dosyasını tarayıcınızda açın.  
