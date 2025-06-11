
# 📱 Android komponensek részletezése: Activity, Service, BroadcastReveiver, ContentProvider. 

Egy Android-alkalmazás **négy alapvető komponensből** épülhet fel: /  önállóan is működő részek,de legtöbbször együtt használjuk őket, hogy teljes, jól működő alkalmazást alkossanak./

---

## 1. Activity – Felhasználói felület -Az Activity mindig a felhasználói felületet kezelő komponens.
Az **Activity** a képernyőn megjelenő felület, ahol a felhasználó interakcióba lép az alkalmazással.
**Az Android alkalmazás egyik fő komponense az Activity , mely a Fragment osztállyal együtt biztosítják a felhasználói felületet.**
**Egy alkalmazáshoz több Activity és több Fragment is tartozhat, ezek összességét UI vezérlőknek hívjuk.**

Az Activity reagál a felhasználói műveletekre (pl. gombnyomás), és saját életciklussal rendelkezik, 
**Egy alkalmazás több Activity-t is tartalmazhat** , melyek különböző képernyőknek felelnek meg, így különféle funkciókat valósítanak meg (pl. login, register, start, gallery vagy egy about).

- Minden Activity-nek önálló életciklusa van / amelyben a rendszer különböző események szerint aktiválja, felfüggeszti vagy megszünteti azt.
   / Ezeket külön életciklus-metódusok (pl. onCreate(), onStart(), onPause() stb.) vezérlik./
- Egy Activity indíthat másikat, és visszalépéskor a stack alapján folytatódik a vezérlés.
- A rendszer egy **Back Stack** nevű veremben kezeli az aktív Activity-ket= „Egy Activity indíthat másikat, és visszalépéskor a stack alapján folytatódik a vezérlés.”
- új Activity létrehozása: Porject panel / Kotlin/+java - jobb katt New Activity / empty views Activity
![image](https://github.com/user-attachments/assets/a6fdd602-6d6e-45be-a32a-1051a8edd0bc)
és itt kiválaszthqaqtod hogy milyen prg kód nylevű legyen: pl: Java  finsh


**MainActivity.java--->>> Fő képernyő működési logikája**
**activity_main.xml---->>	Fő képernyő felhasználói felülete**
![image](https://github.com/user-attachments/assets/8f3644fc-d914-46b6-8677-fbd94703da4d)


---

## 2. Service – Háttérszolgáltatás
- A **Service** a szolgáltatás komponenst háttérben elvégezendő művedletek elvégzésésre használjuk
- **nincs különálló felhasználói felülete**,
- **de  képes** : más komponenseket (pl. Activity) elindítani, vagy külső eseményekre reagálni.
Például egy torrent kliens képes a háttérben működve letölteni az adatokat, miközben a felhasználó bármi mást csinálhat a telefonjával.
Az Android rendszer alapértelmezetten is több különböző szolgáltatást futtat a háttérben, ez biztosítja a megfelelő működését.-->
- **Nem áll le, ha az alkalmazás háttérbe kerül.**  (pl. zenelejátszás, letöltés, szinkronizáció).


### Típusai:
- **Foreground service** /Előtér szolgáltatás/– A háttérben fut, de a felhasználó látja, mert értesítést mutat a működésről.  -Látható (pl. zenelejátszás), értesítéssel.
- **Background service** –/ héáttér/  Nem látható, Teljesen láthatatlanul működik, a háttérben.-  (pl. adatmentés).
- **Bound service** /"kötött"/  – 	Olyan szolgáltatás, amelyhez más komponens (akár másik appból is) csatlakozhat, és kétirányú kommunikáció történhet.- 

## Bound Service – Példák és típusok

| Eset                         | Mi történik?                                      | Milyen típusú kapcsolat?            |
|------------------------------|---------------------------------------------------|--------------------------------------|
| Zenelejátszó vezérlő gombok  | Activity ↔ Service: lekérdezi a dalt, vezérli     | Appon belüli Bound Service           |
| Másik alkalmazás kér adatot  | App A Service-t futtat → App B kér tőle adatot   | Két app közötti Bound Service        |

---

## 3. BroadcastReceiver – Eseményfigyelő
A **BroadcastReceiver** komponensek feladata, hogy különféle események hatására aktiválódva, valamilyen feladatot hajtsanak végre. 
Jellemzőjük, hogy nem rendelkeznek felhasználói felülettel, de megjeleníthetnek figyelmeztetéseket és indíthatnak más komponenseket.
(pl. alacsony akkumulátor, új SMS).

- **Nincs saját felhasználói felülete**, de értesítést küldhet vagy komponenseket indíthat.
- A rendszer automatikusan elindítja, ha olyan esemény történik, amit figyel.

"A legtöbb broadcast a rendszer felől érkezik (például az alacsony akkumulátor szint, a kijelző kikapcsolása, stb). Alkalmazások is indíthatnak broadcastokat, így jelezve más alkalmazások számára.
Amikor egy broadcast esemény bekövetkezik az Android rendszer megvizsgálja, hogy mely alkalmazások tartalmaznak olyan BroadcastReciever komponenst, amelyet az esemény érinthet, és elindítja ezeket a komponenseket. "


---

## 4. ContentProvider – Adatmegosztás  - Tartalom szolgáltató komponens
A **ContentProvider** egy speciális Android komponens, amely lehetővé teszi, hogy egy alkalmazás adatokat osszon meg más alkalmazásokkal — szabályozott, biztonságos módon.
- Több alkalmazás is használhatja ugyanazt az adatforrást (pl. névjegyek).
- Az alkalmazásodban lévő adatok más appok által is elérhetők, módosíthatók, ha engedélyezed.
- Nem kell tudni, hogy az adat hol vagy hogyan van eltárolva (pl. SQLite, fájl, webes API), a ContentProvider egy egységes felületet biztosít.

**biztonságos-e?**
Igen, de engedélyezni kell más appok számára az adatokhoz való hozzáférést, különben nem férhetnek hozzá.
A ContentProvider egy szabványos, biztonságos adatkapu az alkalmazások között.
De **a felhasználó kezében van az irányítás**: engedély nélkül nincs hozzáférés.
---

## 🔐 Példa: ITK Tok alkalmazás és névjegyek

Tegyük fel, hogy az **ITK Tok app** szeretne hozzáférni a telefon névjegyeihez.

- Az Android rendszerben a névjegyeket egy beépített ContentProvider kezeli:  
  `content://contacts/people`
- Az alkalmazás a `ContentResolver` segítségével próbál hozzáférni az adatokhoz.

**De ha nem adsz engedélyt** (pl. `READ_CONTACTS`), akkor:
- Az app **nem férhet hozzá** az adatokhoz.
- A rendszer **megvédi a felhasználói adatokat**.

✅ Ez biztosítja, hogy a ContentProvider **csak akkor oszt meg adatot**, ha a **felhasználó azt jóváhagyta**.
  


---

## 🧰 Beépített példák:

| Tartalom         | URI példa                    |
|------------------|------------------------------|
| Névjegyek        | `content://contacts/people`  |
| SMS-ek           | `content://sms/inbox`        |
| Naptárbejegyzések| `content://calendar/events`  |
| Hívásnapló       | `content://call_log/calls`   |



### Intent- Üzenet:  az alkalmazás az Android rendszernek küld azzal a céllal, hogy elindítson egy másik komponenst (pl. Activity, Service, BroadcastReceiver). Az Android rendszer az Intent tulajdonságai alapján dönti el, hogy melyik komponens tudja fogadni azt.
