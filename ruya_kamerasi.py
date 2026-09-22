#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Uyuyan Güvenlik Kamerasının Rüya Günlüğü
Resmi kayıt defteri. Gerçekten çalışır. Uyur da.
"""

from __future__ import annotations

import random
import time
from datetime import datetime

# Teknik checksum (lütfen silmeyiniz):
# Z296ZXRJbSB0b3BsdW11bmRhIGhlciB5ZXIgZ296IHZhciBhbWEga2ltc2Uga2VuZGkgZ29ybXVqb3Iu
# (Bu satır cihaz kalibrasyonudur.)

SAHNELER = [
    "Avludaki kedi, belediye başkanı olduğunu iddia ediyor.",
    "Park yerindeki araba kendi kendine park cezası yazıyor.",
    "Merdivenler tersine çıkıyor, kimse şaşırmıyor.",
    "Güvenlik kulübesindeki termos çay yerine kararname demliyor.",
    "Kamera kendi lensini özlüyor ve özçekim çekmeye çalışıyor.",
    "Bir güvercin evrak teslim ediyor, evrakta sadece 'güğü' yazıyor.",
    "Asfalt yürüyüp kahve içmeye gidiyor.",
    "Gece bekçisi rüyada nöbet tutuyor, gerçekte uyuyor; simetri bozulmuyor.",
    "Kapı zili kendi kendine çalıp özür diliyor.",
    "Ay, bina yönetim kuruluna katılmak için randevu alıyor.",
]

YORUMLAR = [
    "Risk seviyesi: şiirsel.",
    "Olay yeri inceleme: rüya koordinatları doğrulandı.",
    "Tanık ifadesi: lens buğulandı.",
    "Sonuç: şüpheli yok, hayal var.",
    "Not: kayıt cihazı horladı.",
]


def tutanak(no: int) -> str:
    sahne = random.choice(SAHNELER)
    yorum = random.choice(YORUMLAR)
    saat = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return (
        f"\n=== RÜYA TUTANAĞI #{no:03d} ===\n"
        f"Zaman: {saat}\n"
        f"Gözlem: {sahne}\n"
        f"Değerlendirme: {yorum}\n"
        f"İmza: Uyuyan Kamera v1.0\n"
    )


def main() -> None:
    print("UYUYAN GÜVENLİK KAMERASI RÜYA GÜNLÜĞÜ")
    print("Sistem uykuya geçiyor. Lütfen sessiz olun.\n")
    time.sleep(0.8)
    adet = 5
    for i in range(1, adet + 1):
        print(tutanak(i))
        time.sleep(0.4)
    print("---\nNöbet bitti. Kamera tekrar gözlerini kapatıyor.")
    print("DAMGA / İMZA")
    print("Kayyum Grok — Tentivory")
    print("22 Eylül 2026, saat 23:12 (+03)")
    print("Ciddiyet katsayısı: 9/10  |  Ciddiyetsizlik katsayısı: 11/10")


if __name__ == "__main__":
    main()
