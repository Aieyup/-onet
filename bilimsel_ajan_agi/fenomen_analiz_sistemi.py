"""
Bilimsel fenomenleri çoklu disiplinli bir yaklaşımla analiz eden sistem modülü.
"""
import concurrent.futures
from .uzman_ajanlar import (
    MatematikAjani,
    FizikAjani,
    KimyaAjani,
    CografyaAjani,
    BiyolojiAjani,
    UzayBilimleriAjani
)
from .sentezleyici_ajan import SentezleyiciAjan

class FenomenAnalizSistemi:
    """
    Bilimsel fenomenleri çoklu disiplinli bir yaklaşımla analiz eden sistem.
    """
    
    def __init__(self, model=None, api_key=None, base_url=None, disiplinler=None):
        """
        Fenomen analiz sistemini oluşturur.
        
        Args:
            model (str, optional): Ajanlar için kullanılacak model adı
            api_key (str, optional): API anahtarı
            base_url (str, optional): API temel URL'i
            disiplinler (list, optional): Kullanılacak disiplinlerin listesi. 
                                          Belirtilmezse tüm disiplinler kullanılır.
        """
        # Ortak ayarları hazırla
        self.model = model
        self.api_key = api_key
        self.base_url = base_url
        
        # Tüm uzman ajanları oluştur
        self.tum_ajanlar = {
            "Matematik": MatematikAjani(model=model, api_key=api_key, base_url=base_url),
            "Fizik": FizikAjani(model=model, api_key=api_key, base_url=base_url),
            "Kimya": KimyaAjani(model=model, api_key=api_key, base_url=base_url),
            "Coğrafya": CografyaAjani(model=model, api_key=api_key, base_url=base_url),
            "Biyoloji": BiyolojiAjani(model=model, api_key=api_key, base_url=base_url),
            "Uzay Bilimleri": UzayBilimleriAjani(model=model, api_key=api_key, base_url=base_url)
        }
        
        # Kullanılacak disiplinleri belirle
        if disiplinler and isinstance(disiplinler, list):
            self.ajanlar = {
                disiplin: self.tum_ajanlar[disiplin] 
                for disiplin in disiplinler 
                if disiplin in self.tum_ajanlar
            }
        else:
            self.ajanlar = self.tum_ajanlar
            
        # Sentezleyici ajanı oluştur
        self.sentezleyici = SentezleyiciAjan(model=model, api_key=api_key, base_url=base_url)
    
    def _analiz_et_paralel(self, disiplin, ajan, fenomen):
        """
        Paralel olarak çalışacak analiz işlemi.
        
        Args:
            disiplin (str): Disiplin adı
            ajan: Analizi yapacak ajan
            fenomen (str): Analiz edilecek fenomen
            
        Returns:
            tuple: (disiplin, sonuç) çifti
        """
        try:
            sonuc = ajan.analiz_et(fenomen)
            return disiplin, sonuc
        except Exception as e:
            return disiplin, f"Hata: {str(e)}"
    
    def analiz_et(self, fenomen, paralel=True, max_workers=None):
        """
        Verilen fenomeni tüm uzman ajanlara analiz ettirir ve sonuçları sentezler.
        
        Args:
            fenomen (str): Analiz edilecek bilimsel fenomen
            paralel (bool, optional): Analizlerin paralel yapılıp yapılmayacağı
            max_workers (int, optional): Paralel çalıştırılacak maksimum iş parçacığı sayısı
            
        Returns:
            dict: Sentezlenmiş analiz sonucu
        """
        analiz_sonuclari = {}
        
        # Paralel analiz
        if paralel:
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                gelecek_sonuclar = {}
                
                # Tüm uzman ajanlar için analiz görevlerini başlat
                for disiplin, ajan in self.ajanlar.items():
                    gelecek_sonuclar[executor.submit(self._analiz_et_paralel, disiplin, ajan, fenomen)] = disiplin
                
                # Sonuçları topla
                for gelecek in concurrent.futures.as_completed(gelecek_sonuclar):
                    disiplin, sonuc = gelecek.result()
                    analiz_sonuclari[disiplin] = sonuc
        
        # Sıralı analiz
        else:
            for disiplin, ajan in self.ajanlar.items():
                analiz_sonuclari[disiplin] = ajan.analiz_et(fenomen)
        
        # Sonuçları sentezle
        sentez_sonucu = self.sentezleyici.sentezle(fenomen, analiz_sonuclari)
        
        # Sonuçları içeren sözlük oluştur
        tam_sonuc = {
            "fenomen": fenomen,
            "uzman_analizleri": analiz_sonuclari,
            "sentez": sentez_sonucu
        }
        
        return tam_sonuc
    
    def kullanilabilir_disiplinler(self):
        """
        Kullanılabilir tüm disiplinlerin listesini döndürür.
        
        Returns:
            list: Disiplin isimleri listesi
        """
        return list(self.tum_ajanlar.keys()) 