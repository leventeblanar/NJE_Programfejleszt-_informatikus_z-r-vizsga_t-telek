# 📱 Android – Activity Életciklusmodell Összefoglaló

Az **Activity** az Android alkalmazások egyik alapegysége, ahol a felhasználói interakció történik. Egy alkalmazás több Activity-ből is állhat, és ezek váltakozva, egymást indítva működnek. Minden Activity-nek van egy **életciklusa**, amit az Android rendszer automatikusan kezel, és különböző állapotváltozásokhoz **callback metódusokat** hív meg.
Az Activity példányokat, nem csaka felhasználó válthatja ki, hanem rendszeres események, pl egy hívás után, vagy az akmulátor lemerülése ...

---

## 🔄 Alapvető állapotok

| Állapot  | Jelentés |
|----------|----------|
| **Running** | Az Activity az előtérben van, aktív, használatban. |
| **Paused**  | Az Activity elveszti a fókuszt, de még látható (pl. egy lebegő ablak fölötte)mini player spoti ha levan zárva a telód. |
| **Stopped** | Az Activity teljesen háttérbe kerül, de még megőriz állapotot. |
| **Finished/Killed** | Az Activity befejeződött vagy az OS törölte a memóriából. |

---

## 🧭 Élettartam típusok

1. **Teljes élettartam**  
   `onCreate()` → `onDestroy()` között tart.  
   Itt történik az erőforrások lefoglalása és felszabadítása.
🎧 Spotify példa:
Amikor elindítod a Spotify-t, létrejön az Activity (onCreate()), és egészen addig „él”, amíg teljesen be nem zárod (onDestroy()). Ez az időszak az Activity „élete”.

3. **Látható élettartam**  
   `onStart()` → `onStop()` között.  
   Az Activity látható a képernyőn (akár részben is), de lehet, hogy nem aktív.
Példa:
Képzeld el, hogy egy videót nézel.
Ekkor hívnak, és a hívás lebegő ablakban megjelenik – a videó még látszik mögötte, de nem kattinthatsz rá.
A videó lejátszó Activity még „látható”, de nem aktív – ez a látható élettartam.

A felhasználó látja, de nem biztos, hogy épp használja.

5. **Előtérben lévő élettartam**  
   `onResume()` → `onPause()` között.  
   Az Activity nem csak látható, de aktív is.
🎧 Spotify példa:
Megnyitod a Spotify-t, lapozgatsz a zenék között, hallgatod a lejátszást – a Spotify teljes képernyőn van, fókuszban, azaz éppen „resumed” állapotban van.

---

## 🔁 Callback metódusok működése
Nézzük sorba elindul egy alkalmazás - 
**A felhasználó elindítja az alkalmazást és közbe jön egy hívás pl.:**
# Elindítjuk az appot: `onCreate()` → `onStart()` → `onResume()`
**1. A felhasználó elindít egy alkalmazást:**

### 🔹 `onCreate (Bundle savedInstanceState)`
**2. Az app megnyitódik**
- Beállítjuk a UI-t `setContentView()`.
- Felhasználói elemek inicializálása (`findViewById()`).

### 🔹 `onStart()`
**3. Az app "started" állapotban lesz, megjelenik a felület a felhasználó számára**
- Az Activity láthatóvá válik.
- Előkészül a felhasználói interakciókra.

### 🔹 `onResume()`
**4. az app készen áll az indításra**
- Az Activity előtérbe kerül, fókuszt kap.
- Ekkor történik pl. videó vagy animáció indítása.
- más események hatására ebben az állapotban marad

**5. Activity is Running!  előtérben és aktív**

# Érkezik egy hívás: `onPause()` → `onStop()`
### 🔹 `onPause()`
**6. hívás hatására leáll az indított applikáció, de még látszódik**
- Előfordul, ha egy új Activity jelenik meg részben/teljesen.
- Rövid idejű mentések, hálózati műveletek.
- Minden elindított erőforrást le kell állítani (pl. kamera).

### 🔹 `onStop()`
**7. hívás átvette az irányítást, másik activity lépett előtérbe**
- Az Activity teljesen eltűnik a képernyőről.
- Itt menthetjük az adatokat és felszabadíthatjuk az erőforrásokat.

# Hívás után visszatérünk: `onRestart()` → `onStart()` → `onResume()`
### 🔹 `onRestart()`
- Akkor hívódik meg, ha az Activity leállítás után újraindul.
**8. felkészül újra az app hogy megnyitjuk, visszatérünk hozzá**
**9. OnStart az app újra képernyőn megjelenik**
**10. OnResume készen áll az indításra**

# VAGY  Kilépünk: `onPause()` → `onStop()` → `onDestroy()`

### 🔹 `onDestroy()`
- Az Activity végleg megszűnik.
- Minden maradék erőforrás felszabadítása (pl. szálak, adatbázis).
Itt az android felszabadítja az erőforrásokat. 
---

## 📚 Példa életciklus forgatókönyvre

1. Elindítjuk az appot: `onCreate()` → `onStart()` → `onResume()`
2. Érkezik egy hívás: `onPause()` → `onStop()`
3. Hívás után visszatérünk: `onRestart()` → `onStart()` → `onResume()`
4. Kilépünk: `onPause()` → `onStop()` → `onDestroy()`

![image](https://github.com/user-attachments/assets/acaaa429-c7aa-4849-9c35-593c8eb2b6b2)

---

## 📌 Fontos tanácsok

- **Mentés & visszaállítás**: mindig ments állapotot `onPause()` vagy `onSaveInstanceState()` metódusban.
- **Erőforráskezelés**: kamerát, szenzorokat, hálózati kapcsolatokat `onPause()` vagy `onStop()` alatt állítsd le, `onResume()` alatt indítsd újra.
- **Gyors metódusok**: `onResume()` és `onPause()` gyakran hívódik → ne legyen bennük lassú művelet.

