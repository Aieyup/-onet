"""
Çoklu Disiplinli Bilimsel Fenomen Analiz Sistemi'nin örnek kullanımı.
"""
import os
import json
from bilimsel_ajan_agi import FenomenAnalizSistemi

# Kullanılmak istenen API anahtarını ayarlayın
# Eğer anahtarınızı ortam değişkeni olarak ayarladıysanız, bu satırı yorum yapabilirsiniz
# os.environ["OPENAI_API_KEY"] = "sizin-api-anahtarınız"
# veya
# os.environ["IO_API_KEY"] = "sizin-io-api-anahtarınız"

# Farklı disiplinler için iointel modelleri
MODEL_CONFIGS = {
    "Matematik": "nvidia/AceMath-7B-Instruct",  # Matematiksel hesaplamalar için
    "Fizik": "meta-llama/Llama-3.3-70B-Instruct",  # Genel bilimsel analiz için güçlü model
    "Kimya": "Qwen/Qwen2.5-32B-Instruct",  # Detaylı açıklamalar için
    "Coğrafya": "mistralai/Mistral-Large-Instruct-2411",  # Büyük bağlamsal bilgi
    "Biyoloji": "deepseek-ai/DeepSeek-R1-Distill-Llama-70B",  # Kapsamlı analiz
    "Uzay Bilimleri": "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8"  # Uzun bağlam
}

def main():
    # Analiz edilecek fenomeni tanımla
    fenomen = """Kutup buzullarının erimesi ile artan su seviyelerinin kıyı ekosistemlerine etkisi, 
    okyanus akıntılarındaki değişimler, bunun atmosferik dolaşıma etkisi ve sonucunda 
    meydana gelen iklim değişikliği kalıpları."""
    
    print("Fenomen Analiz Sistemi başlatılıyor...")
    
    # İsteğe bağlı olarak hangi disiplinlerin kullanılacağını belirleyebilirsiniz
    # Örneğin, sadece belirli disiplinleri kullanmak için:
    # analiz_sistemi = FenomenAnalizSistemi(disiplinler=["Fizik", "Kimya", "Coğrafya"])
    
    # Tüm disiplinleri kullanmak için:
    analiz_sistemi = FenomenAnalizSistemi()
    
    print(f"Kullanılabilir disiplinler: {analiz_sistemi.kullanilabilir_disiplinler()}")
    
    print(f"\nFenomen analiz ediliyor: '{fenomen}'\n")
    
    # Fenomeni analiz et
    # Paralel işlemeyi kapatmak için: analiz_sistemi.analiz_et(fenomen, paralel=False)
    sonuc = analiz_sistemi.analiz_et(fenomen)
    
    # Sonucu görüntüle
    print("\n--- UZMAN AJANLARDAN GELEN ANALİZLER ---")
    for disiplin, analiz in sonuc["uzman_analizleri"].items():
        print(f"\n=== {disiplin} ANALİZİ ===")
        print(analiz)
    
    print("\n\n--- SENTEZ SONUCU ---")
    print(sonuc["sentez"])
    
    # Sonucu dosyaya kaydet
    with open("analiz_sonucu.json", "w", encoding="utf-8") as f:
        json.dump(sonuc, f, ensure_ascii=False, indent=2)
    
    print("\nAnaliz sonucu 'analiz_sonucu.json' dosyasına kaydedildi.")

if __name__ == "__main__":
    main() 