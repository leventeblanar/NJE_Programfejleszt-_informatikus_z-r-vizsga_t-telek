
### 8. Intent felépítése és működése. Implicit és explicit Intent. Activity indítás formái

---

#### 1. Intent felépítése és működése

Az **Intent** az Android rendszer **egyik kulcseleme , egy objektum** , amely lehetővé teszi:

A legtöbb Android rendszerre készült alkalmazás több Activity-vel rendelkezik, és mindegyiknek önálló feladatkör jut.
Az alkalmazáson belül egy másik Activity megnyitásához, vagy egy másik alkalmazás elindításához Intent-ek létrehozására van szükség. 
Az Intent egy olyan objektum, melyet az alkalmazás küld az Android rendszer számára, majd a rendszer az Intent tulajdonságai alapján kiválasztja a megfelelő komponenseket melyek fogadni tudják az Intent-et

lényegre törően:  **az alkalmazás az Android rendszernek küld azzal a céllal, hogy elindítson egy másik komponenst (pl. Activity, Service, BroadcastReceiver). 
Az Android rendszer az Intent tulajdonságai alapján dönti el, hogy melyik komponens tudja fogadni azt.**

### 🧑‍💻 Felhasználói példa – Hogyan működik az Intent?

Képzeld el, hogy megnyitsz egy alkalmazást, például egy rendezvény appot. Ebben az appban van egy „Helyszín megtekintése” gomb. Amikor erre a gombra kattintasz:

- Te csak egy gombot nyomsz meg, de a háttérben...
- Az alkalmazás létrehoz egy Intent-et, amely azt mondja:  
  „Nyisd meg a Google Maps alkalmazást, és mutasd meg ezen a helyen a rendezvényt!”
- Az Android rendszer megnézi, melyik alkalmazás tud térképet megjeleníteni, és megtalálja a Google Maps-et.
- A rendszer elindítja a Google Maps alkalmazást, megadott címmel vagy koordinátákkal.
- Te már látod is a térképen a helyszínt – mindezt egyetlen gombnyomással!

Két fő típusa létezik: **explicit** vagy **implicit**:

- ✅ **Explicit Intent**:  **SecondActivity.class**
  Ebben az esetben **konkrétan megadjuk** a célkomponenst (pl. melyik `Activity`-t vagy `Service`-t szeretnénk elindítani).
  Alkalmazáson belül gyakori 
  Példa:
  ```java
  Intent intent = new Intent(this, SecondActivity.class);
  startActivity(intent);
  ```

- 🌐 **Implicit Intent**:  **Intent.ACTION_VIEW**
  Itt **nem nevezzük meg** konkrétan a célt. Ehelyett egy általános műveletet (action) és opcionálisan adatokat (data) adunk meg, és az Android rendszer maga dönti el, hogy melyik alkalmazás képes kezelni a kérést.  
  Példa:
  ```java
  Intent intent = new Intent(Intent.ACTION_VIEW);
  intent.setData(Uri.parse("https://www.google.com"));
  startActivity(intent);
  ```

---

#### 2. Activity indítás formái

![image](https://github.com/user-attachments/assets/8d1a7e67-51f6-49c2-832d-76f00da93542)


Az `Activity`-k indítása **két fő módon történhet:**

- 📤 **`startActivity()`**  - **startActivity(Intent)**
  Egyszerűen elindít egy új `Activity`-t, **visszatérési érték nélkül**.
  ```java
  Intent intent = new Intent(this, SecondActivity.class);
  startActivity(intent);
  ```
### 🧑‍💻 Felhasználói példa – `startActivity()` használata

Képzeld el, hogy egy utazástervező alkalmazást használsz. A főképernyőn van egy „Új útvonal tervezése” gomb. Amikor rákattintasz, az alkalmazás egyszerűen megnyit egy új képernyőt (Activity-t), ahol megadhatod az úticélokat.

Ez a működés belülről így történik:

```java
Intent intent = new Intent(this, NewRouteActivity.class);
startActivity(intent);
``````
Te csak annyit látsz, hogy új képernyő nyílik meg – az előző nem vár visszajelzést.

- 🔄 **`startActivityForResult()`**  
  Lehetővé teszi, hogy **visszatérési adatokat** fogadj az elindított `Activity`-től.  
  Példa:
  ```java
  Intent intent = new Intent(this, SecondActivity.class);
  startActivityForResult(intent, REQUEST_CODE);
``````

### 🧑‍💻 Felhasználói példa – startActivityForResult() használata

Most képzeld el, hogy ugyanabban az alkalmazásban van egy „Profilkép kiválasztása” lehetőség.
Amikor erre rákattintasz, megnyílik a galéria, és kiválasztasz egy képet. Miután visszatérsz, az új kép megjelenik a profilodon.

Ez úgy történik, hogy az alkalmazás vár visszatérő adatot a megnyitott Activity-től (pl. kép útvonala):

```java
Intent intent = new Intent(this, ImagePickerActivity.class);
startActivityForResult(intent, REQUEST_CODE);
```

Miután kiválasztod a képet, az `ImagePickerActivity` visszaküldi az eredményt, és az alkalmazásod feldolgozza.

---
  #### 3.  Service indítása startService(intent)

A **startService(Intent)** metódus hasonlóan működik, de itt egy állandó futásra tervezett komponensről van szó.
 ```java
Intent intent = new Intent(this, MyService.class);
startService(intent);
 ```
---
#### 4. Broadcast küldése sendBroadcast(intent)

Az alkalmazások üzeneteket küldhetnek a rendszer vagy más komponensek számára broadcast formájában.
 ```java
Intent intent = new Intent();
intent.setAction("com.example.TEST_BROADCAST");
sendBroadcast(intent);
 ```
---
  A `REQUEST_CODE` egy egyedi azonosító, amely segít azonosítani, melyik hívásból érkezett a válasz.

  Az eredmény fogadásához az alábbi metódust kell felüldefiniálni:
  ```java
  @Override
  protected void onActivityResult(int requestCode, int resultCode, Intent data) {
      if (requestCode == REQUEST_CODE && resultCode == RESULT_OK) {
          // feldolgozás
      }
  }
  ```

---
