
# 20. Listák létrehozása – Adapter

A legtöbb alkalmazásban találkozunk olyan felületekkel, amelyek görgethető listát tartalmaznak. Ezek lehetnek egyoszlopos (List) vagy többoszlopos (Grid- általában képek) megjelenítések.

## Görgethető listák hatékony megjelenítése

Nagy adathalmazok esetén (pl. 1000 elem) fontos a hatékony betöltés és megjelenítés. Ennek fő módszerei:

- **Lapozás**: az adathalmazt kisebb részekre (pl. 50 elem) bontjuk, és csak az éppen szükséges lapot töltjük be.
- **Előtöltés**: a következő lapot még azelőtt elkezdjük betölteni, hogy a felhasználó elérné a jelenlegi végét (pl. 40. elemnél).
- **Nézet újrafelhasználás**: nem minden elemhez hozunk létre külön nézetet, csak annyit, amennyi egyszerre látható + néhány extra. A képernyőről eltűnő nézet újrahasznosítható új adatokkal.

Ezek kombinálásával biztosíthatjuk a gyors és zökkenőmentes felhasználói élményt nagy listák esetén is.

## Teljesítményoptimalizálás listáknál

Nagy adathalmaz (pl. 1000 elem) esetén a cél:
- Gyors megjelenítés
- Nincs felesleges adatbetöltés
- Ne legyen észrevehető a töltés


## RecyclerView

A listák létrehozására két osztály áll rendelkezésre,:
- egyszerű listákra használhatjuk a **ListView osztályt**,
- de a legtöbb esetben érdemes a **RecyclerView osztályt** használni.

- A RecyclerView a ListView osztály egy fejlettebb és flexibilisebb verziója, beépítetten támogatja a nézetek újrahasznosítását, ezáltal jobb teljesítményt biztosít nagy adathalmazoknál.
**A RecyclerView egy nagy teljesítményű komponens listaelemek kezeléséért felelős**
  
### Fő komponensei:

1. **Minden listához szükséges egy Adapter-t definiálni, amely a biztosítja a kapcsolatot az adatok és a megjelenített nézetek között**  `Adapter`: Kapcsolat az adatforrás és a nézetek között
- nézetek létrehozása, újrafelhasználása és az adatok frissítése
RecyclerView.Adapter

2. A működéshez szükséges még a listához tartozó ViewHolder osztály létrehozása  - Nézetkonténer,
- egyes lista elemeket tartalmazza - csökkenti  a memórai haszn., mert nem hoz létre új nézetet minden elemhez


 3. `LayoutManager`: a lista elemek elrendezéséért felelős - (lineáris, rácsos, stb.)

## Adapter: A RecyclerViey-hoz szükséges adapter, amely a megjelnítendő adatokat és a ViwvHolder-ket köti össze: 

Az `onCreateViewHolder` hozza létre a nézeteket, míg az `onBindViewHolder` beállítja az adatokat a megjelenítéshez.
`getItemCount()` –  visszaadja az adatok számát, amely megmondja RecyclerView-nak hány elemet kell megjelnítenie.

## 🔄 RecyclerView Adapter működése

A `RecyclerView` használatához saját adapter osztályt kell létrehoznunk, amely a `RecyclerView.Adapter`-ből öröklődik.  
Az adapter felel a nézetek létrehozásáért, újrafelhasználásáért és az adatok frissítéséért.  
Szükség van egy `ViewHolder` osztályra is, amely a lista egy elemét reprezentálja.  

### 📋 Lépések RecyclerView létrehozásához:

1. **XML layoutban RecyclerView definiálása**
   ```xml
   <androidx.recyclerview.widget.RecyclerView
       android:id="@+id/recyclerView"
       android:layout_width="match_parent"
       android:layout_height="match_parent" />
   ```

2. **LayoutManager beállítása** (Java példa):
   ```java
   recyclerView.setLayoutManager(new LinearLayoutManager(context));
   ```

3. **Adapter + ViewHolder létrehozása**
   - Készíts saját adapter osztályt, amely örökli a `RecyclerView.Adapter`-t.
   - Hozd létre a `ViewHolder` osztályt az egyes sorok nézeteihez.

4. **Adapter csatolása RecyclerView-hoz**
   ```java
   recyclerView.setAdapter(myAdapter);
   ```


### Egyéb típusok:

- **ListActivity** – Teljes képernyőn megjelenítésére szolgáló Activity-t biztosító list- beépített:  `ListView`-val  - fejlesztő részről: Adatforrás kell hozzá bizts. -
- 
- **ListFragment** – hasonló, mint a ListActivity, csak itt Fragment-en belül.  beépített:  `ListView`-val , Fragment-hez méltóan, rugalmasság és újrafelhasználhatóság

  


