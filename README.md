# Çoklu Disiplinli Bilimsel Fenomen Analiz Sistemi

## Genel Bakış

Bu proje, karmaşık bilimsel fenomenleri analiz etmek için geliştirilmiş yenilikçi ve çok disiplinli bir yapay zeka sistemidir. Sistem, farklı bilimsel disiplinlerde (matematik, fizik, kimya, biyoloji, coğrafya ve uzay bilimleri) uzmanlaşmış ajanları orkestrasyon katmanı aracılığıyla koordine ederek, kapsamlı ve derinlikli analiz sonuçları üretmektedir.

IO.net platformu ve iointel kütüphanesi üzerine inşa edilen bu sistem, paralel işleme kabiliyeti ile yüksek performanslı, genişletilebilir ve esnek bir çözüm sunmaktadır.

## Temel Özellikler

- **Çoklu Disiplinli Analiz**: 6 farklı bilimsel disiplinden uzman ajanlar ile kapsamlı analiz
- **Paralel İşleme**: ThreadPoolExecutor kullanarak eşzamanlı analizler ile hızlı sonuç üretimi
- **İleri Düzey Sentezleme**: Disiplinler arası bağlantılar kuran entegre sonuçlar
- **Özelleştirilebilir Yapı**: Farklı LLM modelleri ve disiplin seçenekleri ile uyarlanabilir sistem
- **Yapılandırılmış Çıktı**: Makine tarafından işlenebilir formatta sunulan analiz sonuçları
- **Yüksek Ölçeklenebilirlik**: Yeni uzman ajanlar ekleyerek genişletilebilir mimari

## Teknolojik Altyapı

Sistem, son teknoloji yapay zeka modelleri ve yazılım mimarisi prensipleri üzerine inşa edilmiştir:

- **Büyük Dil Modelleri**: Meta-Llama/Llama-3.3-70B-Instruct (varsayılan) başta olmak üzere çeşitli LLM'ler
- **Dağıtık İşleme**: ThreadPoolExecutor ile paralel işleme yeteneği
- **Modüler Tasarım**: Kolay genişletilebilir ve bakımı yapılabilir kod tabanı
- **Güvenilir Hata Yönetimi**: Kapsamlı try-except blokları ile sağlam çalışma garantisi

## Kurulum

Sistemi kullanmak için aşağıdaki adımları izleyin:

```bash
# Depoyu klonlayın
git clone https://github.com/kullanici/coklu-disiplinli-fenomen-analiz.git
cd coklu-disiplinli-fenomen-analiz

# Gerekli paketleri yükleyin
pip install -r requirements.txt

# API anahtarınızı ayarlayın
export OPENAI_API_KEY="sizin-api-anahtarınız"
# veya
export IO_API_KEY="sizin-io-api-anahtarınız"
```

## Hızlı Başlangıç

```python
# Örnek kullanım
from bilimsel_ajan_agi import FenomenAnalizSistemi

# Analiz edilecek fenomeni tanımlayın
fenomen = "Küresel iklim değişikliğinin okyanus akıntılarına etkisi"

# Analiz sistemini başlatın
analiz_sistemi = FenomenAnalizSistemi()

# Analiz işlemini gerçekleştirin (paralel analiz için)
sonuc = analiz_sistemi.analiz_et(fenomen, paralel=True)

# Sonuçları görüntüleyin
print(sonuc)

# Sonuçları dosyaya kaydedin (opsiyonel)
import json
with open("analiz_sonucu.json", "w", encoding="utf-8") as f:
    json.dump(sonuc, f, ensure_ascii=False, indent=4)
```

## Bilimsel Ajan Ekosistemi

Sistem şu uzman ajanları içermektedir:

- **Matematik Ajanı**: Matematiksel modelleme, formüller, istatistiksel analizler
- **Fizik Ajanı**: Fizik kanunları, enerji, kuvvet, termodinamik ve dalga mekaniği
- **Kimya Ajanı**: Kimyasal bileşikler, reaksiyonlar, moleküler yapılar, termodinamik
- **Coğrafya Ajanı**: Coğrafi dağılım, iklim faktörleri, topografya, hidroloji
- **Biyoloji Ajanı**: Biyolojik sistemler, ekoloji, genetik, fizyoloji, evrim
- **Uzay Bilimleri Ajanı**: Astronomi, kozmoloji, gezegen bilimi, astrofizik

Her bir ajan, kendi disiplinindeki en güncel bilimsel bilgiler ışığında analiz yapma kabiliyetine sahiptir.

## Sistem Mimarisi ve Algoritması

Sistem, üç ana katmandan oluşan sofistike bir mimari yapıya sahiptir:

1. **Uzman Ajanlar Katmanı**: Her bir bilimsel disiplin için özelleştirilmiş yapay zeka ajanları
2. **Sentezleme Katmanı**: Farklı disiplinlerden gelen analizleri bütünleştiren sentezleyici ajan
3. **Orkestrasyon Katmanı**: Tüm sistem bileşenlerini koordine eden merkezi yönetim birimi

Daha detaylı teknik bilgi için [SISTEM_OZETI.md](SISTEM_OZETI.md) dosyasını inceleyebilirsiniz.

## Uygulama Alanları

Bu güçlü analiz sistemi, aşağıdaki alanlarda önemli katkılar sağlayabilir:

- **İleri Düzey Bilimsel Araştırmalar**: Karmaşık fenomenlerin çok boyutlu analizi
- **Akademik Çalışmalar**: Disiplinler arası bağlantılar kurma ve bilgi sentezleme
- **Eğitim Teknolojileri**: Öğrencilere bütünsel bilimsel bakış açısı kazandırma
- **Endüstriyel Ar-Ge**: Çok boyutlu problemlere yenilikçi çözümler geliştirme(Savunma Sanayi)
- **Politika Geliştirme**: İklim değişikliği gibi karmaşık konularda karar verme süreçlerine destek
- **Sürdürülebilirlik Analizleri**: Çevresel etki değerlendirmeleri ve ekosistem analizleri

## Dosya Yapısı

```
├── README.md                      # Projenin ana açıklaması
├── SISTEM_OZETI.md                # Sistem yapısının detaylı teknik açıklaması
├── bilimsel_ajan_agi/             # Ana paket
│   ├── __init__.py                # Paket başlatma dosyası
│   ├── fenomen_analiz_sistemi.py  # Ana sistem sınıfı ve orkestrasyon
│   ├── sentezleyici_ajan.py       # Sentezleme işlemlerini yürüten ajan
│   └── uzman_ajanlar.py           # Farklı disiplinlerdeki uzman ajanlar
├── ornek_kullanim.py              # Örnek kullanım senaryoları
├── requirements.txt               # Bağımlılıklar
└── setup.py                       # Paket kurulum dosyası 
```

## Katkıda Bulunma

Projeye katkıda bulunmak isteyenler için:

1. Bu depoyu fork edin
2. Yeni bir özellik dalı oluşturun (`git checkout -b yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik: özet'`)
4. Dalınızı push edin (`git push origin yeni-ozellik`)
5. Bir Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında dağıtılmaktadır. Detaylar için [LICENSE](LICENSE) dosyasını inceleyebilirsiniz.


