# 🖼️Felület létrehozása. Vezérlőelemek. View. Felugró értesítések. 


## 🧩 Vezérlők

A vezérlők olyan felületi elemek, amelyek a felhasználónak információt jelenítenek meg, információt kérnek be (pl. szövegbeviteli mező), vagy reagálnak valamilyen eseményre (érintés, gesztus).

 ős típusát: a **View** osztályt.

### 📦 3.3.1. View

A felületen elhelyezhető elemek őse a `View` osztály, amely egy téglalapnyi terület kirajzolásáért, és azon belül az események kezeléséért felel.  
Minden UI vezérlőelem (**widget**), mint a `Button`, `TextView`, `EditText`, stb., ebből származik, így megkapják annak tulajdonságait és viselkedését.

A `View` egyik legfontosabb leszármazottja a **ViewGroup**, amely minden **layout** (elrendezés) ősosztálya.

> A layout-ok olyan speciális vezérlők, amelyek más vezérlők elrendezését segítik a felületen, a saját szabályrendszerük szerint.

Egy `ViewGroup` több `View`-t vagy más `ViewGroup`-okat is tartalmazhat.

---

### 🔖 View tulajdonságai

Az egyik legfontosabb tulajdonság az **azonosító** (`id`).  
Minden vezérlőelemhez rendelhető egyedi `id`, amely lehetővé teszi, hogy Java/Kotlin kódból elérjük és módosítsuk őket futásidőben (pl. szöveg csere).

> Nem minden esetben szükséges azonosítót adni – például, ha egy szöveg nem változik, az `id` elhagyható. Viszont elrendezést befolyásoló vezérlőknél még ekkor is lehet rá szükség.

#### Azonosító beállítása XML-ben:

```xml
<View
    android:id="@+id/main_view"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content" />
```

---

### 📏 Méretezés és térközök

- **layout_width** – az elem szélessége  
- **layout_height** – az elem magassága  
- **padding** – belső térköz (az elem tartalma és a széle között)  
- **margin** – külső térköz (az elem széle és más elemek között)

### Vezérlők: 

| Típus         | Leírás |
|---------------|--------|
| `TextView`    | ha nincs aláhúzva, akkor megjelenő szöveg- Lehet : Statikus használat (csak megjelenít egy szöveget) vagy . Dinamikus használat (pl. üdvözlő szöveg programból) itt MainActivity.java is hozzá

![image](https://github.com/user-attachments/assets/49cc34a8-2849-40aa-90a2-2a651d50b753)

| Típus         | Leírás |
|---------------|--------|
| `EditText`    | In put mező Szövegbevitel felhasználó által pl: név, email, jelszó beviteli mező |

![image](https://github.com/user-attachments/assets/e30352f1-e049-4fa6-863b-887a6d4f7ffe)

| Típus         | Leírás |
|---------------|--------|
| `Button`      | Gomb, kattintásra eseményt vált ki, Feladata: Egy művelet elindítása kattintásra. |

![image](https://github.com/user-attachments/assets/9b894cd8-af4e-4d18-b948-03feb972c750)
![image](https://github.com/user-attachments/assets/96fb1552-040c-4445-97a3-4ddfaf04a1d9)

érdemes megemlíteni a +FloatActionButton-t melyhez a drawable/new/vectro Asset/ nál kershetünk vekort a gombunknak pl, ha egyedit szeretnénk

| Típus         | Leírás |
|---------------|--------|
| `ImageView`   | Képek megjelenítése, logók, ikonok, profilképek PNG JPG SVG |

A projekt res/drawable vagy res/mipmap mappájába
Ha több méretben is elérhető a kép: drawable-mdpi, drawable-hdpi, drawable-xhdpi, stb.
statikus képek → drawable 
alkalmazásikonok → mipmap mappába
**Képnevek: csak kisbetű, szám, aláhúzás (profil_kep.png) – szóköz, ékezet tilos!**


| Típus         | Leírás |
|---------------|--------|
| `CheckBox`    | Több elem közül többet is választható  pl. „Elfogadom a feltételeket” vagy több kedvenc kiválasztása |
| `RadioButton` | Egyszerre csak egy választható egy meghatázozott értékhalmazból  (RadioGroup-pal együtt) |
| `Spinner`     | Legördülő listából egy választása egy meghatázozott értékhalmazból : országválasztás, év kiválasztása |
| `ProgressBar` | Folyamat vizuális jelzése. (határozott vagy határozatlan állapotban) fájlletöltés, adatfeldolgozás |
**két módban használjuk:**

- **indeterminate**határozatlan:  – nem tudjuk meddig fut a folyamat. 
- **determinate** – értesítést adunka  folyamatról- egyfájl letöltése - popablak

## 🔔 Felugró értesítések
### Toast

Felugró üzenetek, ablakok létrehozására több lehetőségünk is van Androidban. Legegyszerűbb formája a **Toast**, amely rövidebb vagy hosszabb ideig felugró üzenetet jelenít meg.  
A megjelenítés idejét a `Toast.makeText()` függvény harmadik paramétere szabályozza:

- `Toast.LENGTH_SHORT`
- `Toast.LENGTH_LONG`

**Példa:**
```java
Toast.makeText(getApplicationContext(), "Toast message", Toast.LENGTH_SHORT).show();
```

Szöveges üzeneten túl akár saját felületet is hozzárendelhetünk a Toast-hoz.  
A `setView()` függvénnyel egy előre definiált és paraméterezett `View`-t jeleníthetünk meg a Toast objektumban.

---

### Dialog -

A **dialógusablakokkal** információt jeleníthetünk meg, döntési lehetőséget adhatunk, vagy adatokat kérhetünk be a felhasználótól.  
Nem foglalják el a teljes képernyőt, és általában akkor használjuk, ha a felhasználó beavatkozása szükséges az alkalmazás működéséhez. Az összes dialógus őse a `Dialog` osztály.

**Típusai:**

- **AlertDialog** – Címmel, gombokkal, listás megjelenítéssel vagy akár teljesen testreszabott felülettel.
- **DatePickerDialog** – Dátum kiválasztására szolgál.
- **TimePickerDialog** – Idő kiválasztására szolgál.

![image](https://github.com/user-attachments/assets/5a04b8e0-0793-48c8-92fa-ee594b633692)


---

🎯 **Tipp**: Soha ne használj fix (px) méreteket, hanem `dp` és `sp` egységeket! Használj `wrap_content` és `match_parent` értékeket az elrendezéshez, és tesztelj különböző képernyőméreteken emulátorban is.







## Vezérlő elemek
Egy vezérlő elem egy olyan View objektum, amely a felhasználóval való közreműködésre szolgáló interfész. 
Az Android biztosít néhány teljesen implementált vezérlő elemet (gombok, választó mezők, szövegbeviteli mezők), ezekkel gyorsan építhető egy UI (felhasználói interfész)
nézzük sorban: 



## ⚙️ Példa View létrehozása és eseménykezelése

XML:
```xml
<View 
  android:id="@+id/main_view"
  android:layout_width="400dp"
  android:layout_height="200dp" />
```

Java:
```java
final View mainView = findViewById(R.id.main_view);
mainView.setOnClickListener(new View.OnClickListener() {
  @Override
  public void onClick(View v) {
    int color = Color.rgb(
      new Random().nextInt(256),
      new Random().nextInt(256),
      new Random().nextInt(256));
    mainView.setBackgroundColor(color);
  }
});
```


