"""
Çoklu Disiplinli Bilimsel Fenomen Analiz Sistemi
"""

from .fenomen_analiz_sistemi import FenomenAnalizSistemi
from .uzman_ajanlar import (
    MatematikAjani,
    FizikAjani,
    KimyaAjani,
    CografyaAjani,
    BiyolojiAjani,
    UzayBilimleriAjani
)
from .sentezleyici_ajan import SentezleyiciAjan

__version__ = "0.1.0"
__all__ = [
    "FenomenAnalizSistemi",
    "MatematikAjani",
    "FizikAjani",
    "KimyaAjani",
    "CografyaAjani",
    "BiyolojiAjani",
    "UzayBilimleriAjani",
    "SentezleyiciAjan"
] 