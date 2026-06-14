# PyGraph - Edytor Graficzny w Pythonie 

PyGraph to nowoczesna, wielowarstwowa aplikacja desktopowa do edycji grafiki, napisana w Pythonie. Wykorzystuje bibliotekę `customtkinter` do renderowania nowoczesnego interfejsu (Dark Mode) oraz zaawansowane możliwości bibliotek `Pillow` i `rembg` do obróbki obrazu i sztucznej inteligencji.

Aplikacja oferuje funkcjonalności znane z profesjonalnych programów graficznych, takie jak obsługa warstw, skróty klawiaturowe czy inteligentne usuwanie tła.

## Główne funkcje

* **Wielowarstwowy silnik (Layers System):** * Dodawanie pustych warstw oraz wstawianie obrazów z dysku jako nowe warstwy.
  * Zmiana kolejności, ukrywanie (widoczność), usuwanie oraz edycja nazw warstw.
  * Suwak przezroczystości (Opacity) dla każdej warstwy niezależnie.
* **Usuwanie tła AI:** Zintegrowany model AI (`rembg`) pozwalający na wycięcie tła z dowolnej warstwy jednym kliknięciem.
* **Narzędzia interaktywne:**
  * ✋ **Przesuń:** Swobodne pozycjonowanie obrazu na warstwie.
  * 🖌 **Pędzel:** Rysowanie z regulacją grubości i koloru.
  * 🔤 **Tekst:** Wstawianie napisów z pełną kontrolą wielkości czcionki.
  * ⬜ **Prostokąt:** Rysowanie figur geometrycznych.
* **Dopasowania i Filtry:**
  * Płynna regulacja w czasie rzeczywistym: Jasność, Kontrast, Nasycenie, Ostrość oraz Skala.
  * Gotowe filtry: Czarno-biały, Rozmycie (Blur), Wyostrzanie, Negatyw, Płaskorzeźba, Detekcja krawędzi.
* **Globalne kadrowanie:** Narzędzie do precyzyjnego (myszką lub co do piksela) przycinania całego płótna roboczego.
* **Historia operacji:** Wbudowany system cofania zmian (Undo), zapamiętujący 8 ostatnich stanów projektu.
* **Wielojęzyczność:** Aplikacja automatycznie wykrywa język systemu lub pozwala na ręczne przełączenie (Polski / Angielski).

## Skróty klawiaturowe (wzorowane na standardach branżowych)

Praca z PyGraph jest szybka i intuicyjna dzięki wbudowanym skrótom (działają z klawiszem `Ctrl` na Windows/Linux oraz `Cmd` na macOS):

* `Ctrl/Cmd + O` - Otwórz projekt
* `Ctrl/Cmd + S` - Zapisz / Eksportuj obraz
* `Ctrl/Cmd + Z` - Cofnij (Undo)

**Narzędzia (aktywowane jednym klawiszem):**
* `V` - Przesuń (Move)
* `B` - Pędzel (Brush)
* `T` - Tekst (Text)
* `R` - Prostokąt (Rectangle)
* `C` - Kadrowanie (Crop)

## Wymagania i instalacja

Aby uruchomić aplikację lokalnie, upewnij się, że masz zainstalowanego Pythona (wersja 3.8+). 

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/daniel-kaliski/PyGraph.git
   cd PyGraph
2. Zainstaluj wymagane biblioteki:
   ```bash
   pip install customtkinter Pillow rembg
3. Uruchom aplikację:
   ```bash
   python PyGraph.py

## Użyte technologie

CustomTkinter: Nowoczesny, wspierający motywy interfejs graficzny.

Pillow (PIL): Główny silnik przetwarzania siatki pikseli, manipulacji kanałem Alpha i kompozycji obrazu.

rembg: Narzędzie uczenia maszynowego do precyzyjnego usuwania tła.

## Zrzut ekranu
<img width="1512" height="1040" alt="Zrzut ekranu 2026-06-14 o 17 47 35" src="https://github.com/user-attachments/assets/30b1ac59-28a3-4f78-90c0-2494a252d709" />


## Licencja
Ten projekt jest udostępniany na licencji GNU General Public License v3.0 (GPL-3.0). Szczegółowe informacje znajdują się w pliku LICENSE lub na stronie opensource.org/license/gpl-3.0.

Autor: Daniel Kaliski
