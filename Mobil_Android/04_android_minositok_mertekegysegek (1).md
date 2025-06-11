
# Android minősítők és mértékegységek – összefoglaló

## 📌 1. Minősítők (Qualifiers) . Kiegészítő jelölés
Amikor futtatunk egy alkalmazást, akkor az Android először az eszköz paramétereinek megfelelő módosítókkal ellátott erőforrásokat próbálja használni. Ha nem talál ilyet, akkor az alapértelmezett erőforrást használja, és az adott képernyő mérethez és sűrűséghez igazodva nagyítja, vagy kicsinyíti az adott elemet. A legjobb megjelenés elérése érdekében azonban a rendszer néha eltér ettől a szabálytól és az alapértelmezett erőforrás helyett egy másik felbontás specifikus erőforrást használ. 

Az Android többféle telefonon fut – kicsin, nagy képernyőn, különböző nyelveken, nappal vagy éjszaka.
**A rendszer úgy dönt, hogy melyik fájlt használja, attól függően:**
mekkora a képernyő,
milyen a tájolás,
milyen a nyelv,
milyen a pixelsűrűség stb.

Itt jönnek képbe a minősítők.
A minősítő egy olyan kiegészítő jelölés, amelyet az Android erőforrásmappák nevéhez adunk hozzá,
**hogy jelezzük, milyen körülmények között (pl. képernyőméret, nyelv, tájolás) szeretnénk egy adott erőforrást (pl. layout, kép, szöveg) használni.**

### 🗂️ Minősítő mappák példái

| Könyvtár neve                   | Minősítők                     |
|--------------------------------|-------------------------------|
| `layout/`                      | nincs                         |


A felhasználói felület megtervezéséhez fontos ismernünk az Android által figyelembe vett jellemzőket:

- **Képernyőméret**: Az eszköz fizikai képátlóját jelenti.  
  Értékei: `small`, `normal`, `large`, `xlarge`.

- **Képernyősűrűség**: A pixelek száma egy adott fizikai területen (általában `dpi`, azaz dots per inch).  
  Értékei: `ldpi`, `mdpi`, `hdpi`, `xhdpi`, `xxhdpi`, `xxxhdpi`.

- **Orientáció**: Az eszköz elhelyezkedése lehet álló (`portrait`) vagy fekvő (`landscape`),  
  és ez futásidőben is megváltozhat.

- **Felbontás**: A képernyőn található fizikai pixelek száma.  
  A felület kialakításánál azonban **a képernyőméretet és pixelsűrűséget** használjuk, nem közvetlenül a felbontást.

---

## 📱 3. Képernyőméret minősítők

| Minősítő | Minimum méret (dp)         |
|----------|-----------------------------|
| small    | 426dp × 320dp               |
| normal   | 470dp × 320dp (kb. 5" telefon) |
| large    | 640dp × 480dp               |
| xlarge   | 960dp × 720dp (kb. 10" tablet) |

---

## 🎨 4. Pixelsűrűség minősítők

| Minősítő   | Méretarány |
|------------|------------|
| ldpi       | 0.75x      |
| mdpi       | 1.0x       |
| hdpi       | 1.5x       |
| xhdpi      | 2.0x       |
| xxhdpi     | 3.0x       |
| xxxhdpi    | 4.0x       |

> A rendszer automatikusan kiválasztja a megfelelő felbontású képet (pl. ikon) az `drawable-xxhdpi` mappákból.

---

## 🧩 5. Minősítők általános formája

```text
<resource_name>-<qualifier1>-<qualifier2>-...
```

Például: `layout-large-land-night`

---

## 📏 6. Mértékegységek az Androidban

Az Android többféle mértékegységet támogat, de felülettervezéshez **a következő kettő a legfontosabb**:

| Mértékegység | Jelentés                              | Használat                        |
|--------------|----------------------------------------|----------------------------------|
| `dp`         | sűrűségfüggetlen pixel- Olyan egység, amely független a képernyő pixelsűrűségétől (dpi)                 | vezérlők mérete, padding, margin |
| `sp`         | skálafüggetlen pixel (betűméret)  Az sp a dp-hez hasonló, de figyelembe veszi a felhasználó beállításait is, különösen a betűméret módosítást.

Ez azt jelenti, hogy ha a felhasználó nagyobb betűméretet állít be a készüléken, az sp-ben megadott szövegek is arányosan nőnek.     | szövegek mérete                  |

> A `dp` és `sp` segít egységes megjelenést biztosítani különböző képernyőméreteken és felbontásokon.

Támogatott egyéb mértékegységek:
- `px` – pixel
- `in` – inch (hüvelyk)
- `mm` – milliméter
- `pt` – pont

---

## ✅ Összefoglalás

- Minősítők segítenek több képernyőmérethez és beállításhoz igazítani az appot.
- Az Android automatikusan választ a mappák és fájlverziók közül.
- A `dp` és `sp` használatával nem kell minden eszközre külön UI-t készíteni.
- A Merged Manifest fülön láthatjuk, mi kerül végül ténylegesen a rendszerbe.
