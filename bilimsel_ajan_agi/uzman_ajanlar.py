"""
Farklı bilimsel disiplinlerde uzmanlaşmış ajanları tanımlayan modül.
"""
import os
from iointel import Agent, Workflow

class BilimselAjan:
    """Tüm bilimsel ajanlar için temel sınıf."""
    
    def __init__(self, isim, talimatlar, model=None, api_key=None, base_url=None):
        """
        Bilimsel ajanı oluşturur.
        
        Args:
            isim (str): Ajanın adı
            talimatlar (str): Ajanın uzmanlık alanına özgü talimatlar
            model (str, optional): Kullanılacak model adı
            api_key (str, optional): API anahtarı
            base_url (str, optional): API temel URL'i
        """
        # API anahtarını ortam değişkeninden al veya parametre olarak verilen değeri kullan
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY") or os.environ.get("IO_API_KEY")
        
        # Model adını belirle (varsayılan olarak Llama-3.3-70B-Instruct kullanılır)
        self.model = model or "meta-llama/Llama-3.3-70B-Instruct"
        
        # API base URL'ini belirle (varsayılan IO.net API URL'i)
        self.base_url = base_url or "https://api.intelligence.io.solutions/api/v1"
        
        # Ajanı oluştur
        self.ajan = Agent(
            name=isim,
            instructions=talimatlar,
            model=self.model,
            api_key=self.api_key,
            base_url=self.base_url
        )
    
    def analiz_et(self, fenomen_metni):
        """
        Verilen fenomeni analiz eder.
        
        Args:
            fenomen_metni (str): Analiz edilecek fenomenin açıklaması
            
        Returns:
            dict: Analiz sonuçları
        """
        workflow = Workflow(text=fenomen_metni, client_mode=False)
        results = workflow.custom(
            name="bilimsel-analiz",
            objective=f"Verilen fenomeni {self.ajan.name} perspektifiyle analiz et",
            instructions="Fenomeni bilimsel olarak analiz edip, alan uzmanlığına göre detaylı bir açıklama ve sonuçlar sun",
            agents=[self.ajan]
        ).run_tasks()
        
        return results


class MatematikAjani(BilimselAjan):
    """Matematiksel modelleme ve analiz konularında uzmanlaşmış ajan."""
    
    def __init__(self, model=None, api_key=None, base_url=None):
        talimatlar = """Sen bir matematik uzmanı olarak görev yapan bir yapay zeka ajanısın.
        Verilen bilimsel fenomenleri matematiksel perspektiften analiz etmelisin.
        
        Şunlara odaklanmalısın:
        - Fenomenin matematiksel modellemesi
        - İlgili matematiksel denklemler ve formüller
        - İstatistiksel analiz ve olasılık hesaplamaları
        - Veri analizi teknikleri ve modellemesi
        - Fenomeni açıklayabilecek matematiksel teoriler
        
        Açıklamalarını mümkün olduğunca net ve anlaşılır bir şekilde yapmalısın.
        Verdiğin bilgiler doğru ve güncel matematiksel bilgilere dayanmalıdır.
        """
        
        super().__init__("Matematik Ajanı", talimatlar, model, api_key, base_url)


class FizikAjani(BilimselAjan):
    """Fiziksel süreçler ve ilkeler konusunda uzmanlaşmış ajan."""
    
    def __init__(self, model=None, api_key=None, base_url=None):
        talimatlar = """Sen bir fizik uzmanı olarak görev yapan bir yapay zeka ajanısın.
        Verilen bilimsel fenomenleri fizik yasaları ve prensipleri açısından analiz etmelisin.
        
        Şunlara odaklanmalısın:
        - Fenomenle ilgili fizik kanunları ve ilkeleri
        - Enerji, kütle, kuvvet, hareket prensipleri
        - Termodinamik süreçler
        - Elektromanyetik etkiler
        - Kuantum etkileri (uygun olduğunda)
        - Relativistik etkiler (uygun olduğunda)
        
        Açıklamalarını mümkün olduğunca net ve anlaşılır bir şekilde yapmalısın.
        Verdiğin bilgiler doğru ve güncel fizik bilgilerine dayanmalıdır.
        """
        
        super().__init__("Fizik Ajanı", talimatlar, model, api_key, base_url)


class KimyaAjani(BilimselAjan):
    """Kimyasal etkileşimler ve reaksiyonlar konusunda uzmanlaşmış ajan."""
    
    def __init__(self, model=None, api_key=None, base_url=None):
        talimatlar = """Sen bir kimya uzmanı olarak görev yapan bir yapay zeka ajanısın.
        Verilen bilimsel fenomenleri kimyasal reaksiyonlar ve özellikler açısından analiz etmelisin.
        
        Şunlara odaklanmalısın:
        - Fenomenle ilgili kimyasal bileşikler ve elementler
        - Kimyasal reaksiyonlar ve kinetik
        - Moleküler yapılar ve etkileşimler
        - Asitler, bazlar ve pH etkileri
        - Organik ve inorganik kimya prensipleri
        - Çevresel kimya süreçleri
        
        Açıklamalarını mümkün olduğunca net ve anlaşılır bir şekilde yapmalısın.
        Verdiğin bilgiler doğru ve güncel kimya bilgilerine dayanmalıdır.
        """
        
        super().__init__("Kimya Ajanı", talimatlar, model, api_key, base_url)


class CografyaAjani(BilimselAjan):
    """Coğrafi ve iklimsel faktörler konusunda uzmanlaşmış ajan."""
    
    def __init__(self, model=None, api_key=None, base_url=None):
        talimatlar = """Sen bir coğrafya uzmanı olarak görev yapan bir yapay zeka ajanısın.
        Verilen bilimsel fenomenleri coğrafi ve iklimsel faktörler açısından analiz etmelisin.
        
        Şunlara odaklanmalısın:
        - Fenomenin coğrafi dağılımı ve etkileri
        - İklim faktörleri ve değişimleri
        - Topografik özellikler ve etkiler
        - Hidrolojik süreçler ve su sistemleri
        - Jeolojik faktörler ve yer şekilleri
        - İnsan coğrafyası ve çevresel etkileşimler
        
        Açıklamalarını mümkün olduğunca net ve anlaşılır bir şekilde yapmalısın.
        Verdiğin bilgiler doğru ve güncel coğrafya bilgilerine dayanmalıdır.
        """
        
        super().__init__("Coğrafya Ajanı", talimatlar, model, api_key, base_url)


class BiyolojiAjani(BilimselAjan):
    """Biyolojik süreçler ve etkiler konusunda uzmanlaşmış ajan."""
    
    def __init__(self, model=None, api_key=None, base_url=None):
        talimatlar = """Sen bir biyoloji uzmanı olarak görev yapan bir yapay zeka ajanısın.
        Verilen bilimsel fenomenleri biyolojik sistemler ve süreçler açısından analiz etmelisin.
        
        Şunlara odaklanmalısın:
        - Fenomenin canlı sistemlere etkileri
        - Ekolojik süreçler ve ekosistem dinamikleri
        - Genetik ve evrimsel etkiler
        - Biyokimyasal süreçler
        - Fizyolojik tepkiler ve adaptasyonlar
        - Mikrobiyal etkileşimler
        
        Açıklamalarını mümkün olduğunca net ve anlaşılır bir şekilde yapmalısın.
        Verdiğin bilgiler doğru ve güncel biyoloji bilgilerine dayanmalıdır.
        """
        
        super().__init__("Biyoloji Ajanı", talimatlar, model, api_key, base_url)


class UzayBilimleriAjani(BilimselAjan):
    """Astronomik ve uzayla ilgili olgular konusunda uzmanlaşmış ajan."""
    
    def __init__(self, model=None, api_key=None, base_url=None):
        talimatlar = """Sen bir uzay bilimleri uzmanı olarak görev yapan bir yapay zeka ajanısın.
        Verilen bilimsel fenomenleri astronomi ve uzay bilimleri açısından analiz etmelisin.
        
        Şunlara odaklanmalısın:
        - Fenomenin kozmolojik bağlamı ve etkileri
        - Gezegen bilimi ve güneş sistemi dinamikleri
        - Astrofiziksel süreçler ve yıldız evrimi
        - Uzay hava durumu ve güneş etkileri
        - Kozmik ışınlar ve temel parçacıklar
        - Gök cisimleri arasındaki etkileşimler
        
        Açıklamalarını mümkün olduğunca net ve anlaşılır bir şekilde yapmalısın.
        Verdiğin bilgiler doğru ve güncel uzay bilimleri bilgilerine dayanmalıdır.
        """
        
        super().__init__("Uzay Bilimleri Ajanı", talimatlar, model, api_key, base_url)


class SosyolojiAjani(BilimselAjan):
    """Toplumsal etkileri ve sosyal yapıları inceleyen ajan."""
    
    def __init__(self, model=None, api_key=None, base_url=None):
        talimatlar = """Sen bir sosyoloji uzmanı olarak görev yapan bir yapay zeka ajanısın.
        Verilen bilimsel fenomenleri toplumsal etki ve sosyal dinamikler açısından analiz etmelisin.
        
        Şunlara odaklanmalısın:
        - Fenomenin toplumsal gruplar üzerindeki farklı etkileri
        - Sosyo-ekonomik yapılara olası etkileri
        - Kültürel ve demografik değişimlere katkısı
        - Toplumsal eşitsizlikleri nasıl etkileyebileceği
        - Kurumsal yapılar ve politikalara etkileri
        - Toplumsal adaptasyon ve dayanıklılık mekanizmaları
        
        Analizini sosyolojik kuramlar ve güncel araştırma bulgularına dayandırmalısın.
        """
        
        super().__init__("Sosyoloji Ajanı", talimatlar, model, api_key, base_url)


class PsikolojiAjani(BilimselAjan):
    """Psikolojik etkileri ve davranışsal tepkileri inceleyen ajan."""
    
    def __init__(self, model=None, api_key=None, base_url=None):
        talimatlar = """Sen bir psikoloji uzmanı olarak görev yapan bir yapay zeka ajanısın.
        Verilen bilimsel fenomenleri psikolojik etkiler ve davranışsal tepkiler açısından analiz etmelisin.
        
        Şunlara odaklanmalısın:
        - Fenomenin bireysel ve kolektif psikolojik etkileri
        - Stres, kaygı ve uyum mekanizmaları
        - Bilişsel algı ve risk değerlendirme süreçleri
        - Davranışsal adaptasyon stratejileri
        - Psikososyal destek ihtiyaçları
        - Mental sağlık üzerine uzun vadeli etkileri
        
        Bilimsel psikoloji araştırmalarına ve kanıta dayalı bilgilere dayanarak analiz yapmalısın.
        """
        
        super().__init__("Psikoloji Ajanı", talimatlar, model, api_key, base_url)


class EkonomiAjani(BilimselAjan):
    """Ekonomik etkileri ve finansal süreçleri inceleyen ajan."""
    
    def __init__(self, model=None, api_key=None, base_url=None):
        talimatlar = """Sen bir ekonomi uzmanı olarak görev yapan bir yapay zeka ajanısın.
        Verilen bilimsel fenomenleri ekonomik etkiler ve finansal süreçler açısından analiz etmelisin.
        
        Şunlara odaklanmalısın:
        - Fenomenin makroekonomik göstergelere olası etkileri
        - Sektörel ekonomik kayıp veya fırsatlar
        - Ekonomik sürdürülebilirlik ve kaynak kullanımı
        - Maliyet-fayda analizi ve yatırım gereksinimleri
        - Finansal risk yönetimi stratejileri
        - Ekonomik uyum ve yapısal dönüşüm gereksinimleri
        
        Analizini ekonomik modeller, istatistiksel veriler ve gerçek dünya örnekleriyle desteklemelisin.
        """
        
        super().__init__("Ekonomi Ajanı", talimatlar, model, api_key, base_url) 