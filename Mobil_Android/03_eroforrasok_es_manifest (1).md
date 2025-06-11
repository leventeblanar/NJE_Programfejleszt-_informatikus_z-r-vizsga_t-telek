
# 📁 Erőforrás-állományok- RES- resources  és Manifest fájl - Nyilvánvaló  – Rövid összefoglalás

## 📦 Android alkalmazás felépítése 
Egy Android-alkalmazás nem csupán kódból áll, hanem többféle összetevőből, amelyek különböző célokat szolgálnak. 
Ezek együtt alkotják a teljes alkalmazást.
Az erőforrás állományok ilyen elemek, amelyeket az alkalmazőás használ: képek hangok, xml elrendezési fájlok...

## Egy Android alkalmazás fő részei

Egy Android alkalmazás 4 fő részre bontható:

### 1. **Metainformációk**
- `AndroidManifest.xml` – az alkalmazás szerkezeti leírása  
- Ez olyan, mint az alkalmazás **útlevele vagy specifikációja**, amit az Android rendszer használ a telepítés és futtatás során.  
- Tartalmazza például:
  - a csomag nevét
  - a minimálisan szükséges Android verziót
  - deklarált komponenseket (Activity, Service, stb.)

### 2. **Erőforrások** •	res: erőforrásállományok (minden, ami nem forrásállomány) helye: XML layout, szövegek, képek, animációk, hangfájlok, stb. 
- XML fájlokban tárolt adatok, pl.:
  - UI elemek (`layout/`)
  - szövegek (`values/strings.xml`)
  - képek, ikonok (`drawable/`)
  - animációk (`anim/`)

### 3. **Forráskód**
- Az alkalmazás működési logikája, amit **Java** vagy **Kotlin** nyelven írnak.
- Négy fő komponens:
  - **Activity** – a felhasználói felület működtetése
  - **Service** – háttérfeladatok kezelése
  - **BroadcastReceiver** – rendszeresemények figyelése (pl. töltés kezdete)
  - **ContentProvider** – adatmegosztás más alkalmazásokkal

### 4. **Külső könyvtárak**
- Gyakran használnak külső fejlesztésű könyvtárakat, például:
  - **Firebase** – felhőszolgáltatások, adatbázis, hitelesítés stb.

- Ezeket a `build.gradle` fájlban lehet hozzáadni, így az **Android Studio automatikusan letölti és beépíti** a projektbe.


---

## 🎨 Erőforrás-állományok (res= resources mappa)

Az Android egyik előnye, hogy a kód és a felhasználói felület szétválik.
A res (resources) mappában helyezkednek el az erőforrások: XML elrendezési fájlok:

| Könyvtár | Tartalom |
|----------|----------|
| `drawable/` | alkalmazásban használt  Képek, vektorgrafikák |
| `layout/` | Felületet struktúrát-  elrendezések (`activity_main.xml`) |
| `menu/`, `anim/`, `raw/` | Menüelemek, animációk, fájlok |
| `navigation/`, |` navigáció két vagy több fragment között`|
| `values/` | Szövegek, színek, méretek.témák (`strings.xml`, `colors.xml` , styles.xml`) |
| `xml/` | ´felhőben tárolt elemek és adatok |


Ezekből a Java-kód `R.java` (vagy `R.kt`) fájlon keresztül hivatkozhat az erőforrásokra.

---

## 🗂️ AndroidManifest.xml – Az alkalmazás leíró fájlja ez az xml tárolja el a project tulajdonságait
**manifests: alkalmazás manifest állománya (AndroidManifest.xml), amely az engedélyeket, komponenseket, stb. definiálja**
Ez a fájl tartalmaz minden lényeges információt az alkalmazásról:
**tartalmaznia kell az alkalmazás csomagnevét, valamint a verziókódot és verziónevet.**
- **manifest fejléc:** xml verzió, kódolás, utf és az android és eszközök definiálja
- **aplication blokk: Alkalmazás komponensek deklarálása**:
- Alkalmazás neve, ikonja, témája, veziója API Az <application> tagon belül kell felsorolni az egyes alkalmazás komponenseket, - activity, services, boradcastrecervier és contentprovieder
- **activity** több képernyőből melyik az app induló képernyője, ezt itt l ehet beállítani 
- **alkalmazáshoz tartozó engedeélyek**
```xml
  <uses-permission android:name="android.permission.CAMERA" />
    <uses-permission android:name="android.permission.INTERNET"
```
- **Hardverkövetelmények meghatározása**:
```xml
<uses-feature android:name="android.hardware.bluetooth" />
```

A képernyőmérettel kapcsolatosan megadhatunk pár előírást a manifest állományban
A Manifest fájl végleges változatát Android Studio-ban a **"Merged Manifest"** fülön láthatjuk.

---

## 📌 Példa Manifest részlet:


![image](https://github.com/user-attachments/assets/94dc0191-4dc5-4f4d-b8ed-33f0700f2438)



## 🧠 Lényeg:
- Az erőforrások és a forráskód **elkülönülnek**, ami átláthatóbbá teszi a fejlesztést.
- A **Manifest fájl** szabályozza, hogy mit láthat és használhat az Android rendszer az alkalmazásból.
