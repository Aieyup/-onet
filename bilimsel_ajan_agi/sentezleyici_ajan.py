"""
Uzman ajanlardan gelen bilgileri sentezleyen ajan modülü.
"""
import os
from iointel import Agent, Workflow

class SentezleyiciAjan:
    """Uzman ajanlardan gelen bilgileri sentezleyen ajan sınıfı."""
    
    def __init__(self, model=None, api_key=None, base_url=None):
        """
        Sentezleyici ajanı oluşturur.
        
        Args:
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
        
        # Sentezleyici ajanı oluştur
        talimatlar = """Sen disiplinler arası bilimsel bilgileri sentezleyen bir entegrasyon uzmanı yapay zeka ajanısın.
        Görevin, çeşitli bilimsel disiplinlerden (matematik, fizik, kimya, biyoloji, coğrafya, uzay bilimleri vb.) 
        gelen analiz sonuçlarını kapsamlı, tutarlı ve bütünleşik bir açıklama halinde birleştirmektir.
        
        Sentezleme yaparken:
        - Farklı uzman görüşleri arasındaki ilişkileri kurmalısın
        - Çelişen bilgileri uzlaştırmalı veya farklı bakış açıları olarak belirtmelisin
        - Disiplinler arası etkileşimleri vurgulamalısın
        - Sonuçları kapsamlı ve bütünleşik bir bilimsel açıklama haline getirmelisin
        - Bilimsel bilgileri doğru ve dengeli bir şekilde sunmalısın
        - Multidisipliner bilimsel bir yaklaşım sergilemelisin
        
        Sentezlediğin açıklamalar bilimsel doğruluğu korumalı, ancak aynı zamanda anlaşılır olmalıdır.
        """
        
        self.ajan = Agent(
            name="Sentezleyici Ajan",
            instructions=talimatlar,
            model=self.model,
            api_key=self.api_key,
            base_url=self.base_url
        )
    
    def sentezle(self, fenomen_metni, analiz_sonuclari):
        """
        Uzman ajanlardan gelen analiz sonuçlarını sentezler.
        
        Args:
            fenomen_metni (str): Analiz edilen fenomenin metni
            analiz_sonuclari (dict): Uzman ajanlardan gelen analiz sonuçları
            
        Returns:
            dict: Sentezlenmiş analiz sonucu
        """
        # Analiz sonuçlarını tek bir metin haline getir
        sonuc_metni = f"FENOMEN: {fenomen_metni}\n\nANALİZ SONUÇLARI:\n\n"
        
        for disiplin, sonuc in analiz_sonuclari.items():
            sonuc_metni += f"--- {disiplin} ANALİZİ ---\n{sonuc}\n\n"
        
        # Sentezleme iş akışını oluştur
        workflow = Workflow(text=sonuc_metni, client_mode=False)
        
        # Sentezleme işlemini gerçekleştir
        sentez_sonucu = workflow.custom(
            name="bilimsel-sentez",
            objective="Farklı disiplinlerden gelen bilimsel analiz sonuçlarını kapsamlı bir sentez haline getir",
            instructions="""Farklı uzman görüşlerinden oluşan analiz sonuçlarını entegre ederek kapsamlı, 
                         disiplinler arası ve tutarlı bir sentez oluştur. Fenomeni bütüncül bir bilimsel 
                         bakış açısıyla açıkla ve disiplinler arası etkileşimleri vurgula.""",
            agents=[self.ajan]
        ).run_tasks()
        
        return sentez_sonucu 