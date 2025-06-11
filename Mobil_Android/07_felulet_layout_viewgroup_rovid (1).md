## 17. Felület létrehozása – Layout, ViewGroup

A vezérlők olyan UI elemek, amelyek adatot jelenítenek meg, kérnek be, vagy eseményekre reagálnak. Ezek ősosztálya a View, amely felelős a kirajzolásért és az interakciók kezeléséért. A ViewGroup a View egyik fontos leszármazottja, amely elrendezési szabályok alapján rendezi el a vezérlőket a felületen.

![image](https://github.com/user-attachments/assets/5b8415e4-594a-4a08-b428-1471b7c4a515)


### ViewGroup

A **ViewGroup** összefogja a View elemeket, layout konténerekből áll (pl. LinearLayout, RelativeLayout, stb.). Mivel az XML-ben csak egy gyökérelem lehet, ViewGroup szükséges több elem kezeléséhez.

### Layout elemek: 
**A vezérlők csak a felület egy részét alkotják, ezért szükség van olyan elemre is, amely elrendezi őket – ezt nevezzük layout-nak.**
A layout-ok a ViewGroup osztályból származnak, és meghatározzák, hol helyezkedjenek el a vezérlők a képernyőn.
Egy layout más layout-okat is tartalmazhat, így összetett felületek is létrehozhatók.
Activity vagy Fragment esetén az XML gyökéreleme mindig egy layout típusú elem.

### LinearLayout Az elemek sorrendben, **egymás után helyezkednek el** – függőlegesen vagy vízszintesen (orientation) szerint

A LinearLayout az egyik legegyszerűbb és legtöbbett laklamazaott elrendezési típus az Androidban. 
Az orientation attribútum segítségével szabályozható, hogy a UI-elemek (pl. TextView, Button, ImageView stb.):
- egymás alatt (függőlegesen – vertical),
- vagy egymás mellett (vízszintesen – horizontal) jelenjenek meg.

**Közös tulajdonságok is elérhetőek:**
- Támogatott attribútumok: `layout_width`, `layout_height`, `margin`, `padding`, `id`, `background`.
- `gravity`: tartalom igazítása a vezérlőn belül.
- `layout_gravity`: a vezérlő elhelyezése a szülőn belül.
- Súlyozás: `layout_weight` segítségével az elemek arányos elosztása.
- android:orientation="vertical"   / "horizontal"  -->  függőleges/ vizszíntes megjelenése az elemnek

- ![image](https://github.com/user-attachments/assets/90023cd0-7d11-44d2-99c8-53687774aeaf)

pl:

<LinearLayout
    android:id="@+id/linearLayout"
    android:orientation="vertical"   / "horizontal"
    android:layout_width="match_parent"  // az elem pontosan akkora lesz, mint a szülő 
    android:layout_height="wrap_content">  //az elem csak akkora lesz, amekkora a tartalma

**viszont a sok egymásba ágyazás hatására a felületet leíró XML egyre csak gyarapszik olyan elemekkel, melyek csak az elrendezésben vesznek részt, másrészről pedig a felület betöltését lassítja, ha a felületet leíró fa struktúra mélysége egyre nagyobb**

### RelativeLayout

„A RelativeLayout lehetővé teszi az UI **elemek** (pl. TextView, Button, ImageView stb.) **relatív elhelyezését egymáshoz vagy a szülőhöz képest.”**
A vezérlőket más vezérlőkhöz (ennek az a feltétele, hogy a vezérlők azonosítóját be kell állítanunk) vagy a szülő Relative Layout-hoz viszonyítva pozícionálhatjuk a felületen.
Egyszerűbb XML-t és gyorsabb megjelenítést eredményez, mint a többszörösen ágyazott LinearLayout-ok.


### ConstraintLayout létre tudunk hozni komplex felületeket

Modern, hatékony ***layout konténer:**
- Komplex felületekhez is elég egyetlen szülő elem.
- Támogatja a különféle képernyőméretekhez való alkalmazkodást.
- Legalább 1 vízszintes és 1 függőleges constraint szükséges minden View-ra.
- Használható XML-ben és Android Studio Designer-ben is.

- ![image](https://github.com/user-attachments/assets/bb521225-08f8-4c97-9016-894cffd838bc)


**Újdonságok (1.1-es verzió):**
- Méretezés százalékosan.
- Vezérlők összeláncolása (`chain`), különféle típusokkal: Spread, Spread Inside, Weighted, Packed.

![image](https://github.com/user-attachments/assets/1f2e2587-dcd9-4aa3-8f8a-a3bdf33ca7f3)

### 4. FrameLayout

A `FrameLayout` egy egyszerű konténer, amely alapvetően **egyetlen gyermekelem megjelenítésére készült.** 
Ha több UI-elemet adunk hozzá, azok egymás fölé kerülnek, a szülő bal felső sarkából indulva. 
Ezért tipikusan akkor használják, amikor elemeket egymásra szeretnénk helyezni (pl. egy kép fölé szöveget).

- 📌 Hasznos attribútum:  
  `layout_gravity` – szabályozza a gyermek pozícióját a konténeren belül.
  ![image](https://github.com/user-attachments/assets/2a72a041-7ac7-4dc0-9ab7-78036ae10503)

---

### 5. TableLayout

A `TableLayout` táblázatszerű elrendezést biztosít. Az UI-elemek sorokba és oszlopokba rendezhetők, hasonlóan egy HTML-táblázathoz. 
**Minden sor külön `TableRow` objektum, amely további elemeket (pl. `TextView`, `Button`) tartalmazhat.**

- 🔹 Minden sor = `TableRow`
- 🔹 Az oszlopok száma a legszélesebb sor alapján dől el.

---

### 6. GridLayout

A `GridLayout` egy rácsszerű elrendezés, amely lehetővé teszi, hogy az UI-elemeket sorokba és oszlopokba rendezzük. A `TableLayout`-hoz hasonlít, de nagyobb rugalmasságot nyújt – például egy elem több sort vagy oszlopot is elfoglalhat.

- 📌 Fontos attribútumok:
  - `layout_row` – sor megadása
  - `layout_column` – oszlop megadása
  - `layout_rowSpan` – hány sort foglaljon el
  - `layout_columnSpan` – hány oszlopot foglaljon el

---

### 7. AbsoluteLayout

Az `AbsoluteLayout` lehetővé teszi, hogy az elemeket pontos `(x, y)` koordináták alapján helyezzük el. Ez elsőre kényelmesnek tűnhet, de nem rugalmas: a különböző képernyőméretek és felbontások esetén az elrendezés széteshet vagy rosszul jelenhet meg.

- ⚠️ Nem ajánlott használni modern Android fejlesztésben.
- 🚫 Nem skálázódik jól különböző kijelzőkre.

---

