
# Fragmentek és navigáció megvalósítása

## Fragmentek szerepe és működése
Az **Activity** a képernyőn megjelenő felület, ahol a felhasználó interakcióba lép az alkalmazással.
**Az Android alkalmazás egyik fő komponense az Activity , mely a Fragment osztállyal együtt biztosítják a felhasználói felületet.**
**Egy alkalmazáshoz több Activity és több Fragment is tartozhat, ezek összességét UI vezérlőknek hívjuk.**

A **Fragment** Egy Fragment a felhasználói felület részét képezi, és önálló életciklussal rendelkezik,
amely a felhasználói felület egy részét jeleníti meg. 
**Fragmentek hatékonyabbak lehetnek, mint különálló Activity-k, mivel:**

- újrafelhasználhatók,
- kisebb erőforrásigényűek,
- könnyebben kezelhetők egy komplex felületen belül,
- dinamikusan hozhatók létre és cserélhetők le futásidőben.

A Fragmentek önmagukban nem létezhetnek, minden esetben egy **Activity-hez** kell tartozniuk, amely az életciklusukat is befolyásolja.

## 🧩 Fragment-ek szerepe

Egy Activity több Fragment-et is tartalmazhat, és ezek életciklusa az Activity-hez igazodik.  
Fragment-ek különösen hasznosak, ha a felület elrendezése a kijelző méretétől függ – például egy email appnál, ahol kisebb kijelzőn csak a lista vagy az üzenet látszik, nagyobb kijelzőn viszont mindkettő egyszerre.  
Fragment-ekkel rugalmasabb, újrahasznosítható UI komponenseket készíthetünk, felesleges Activity-váltások nélkül.

**A Fragment-ek létrehozása, lecserélése, megsemmisítése tranzakciók keretében történik. A tranzakciók végrehajtása során lehetőség van azok eltárolására egy veremben (back stack)**

## Fragment életciklus és metódusok

**A Fragmentek működése az Activity-khez hasonlóan életciklus metódusokon keresztül valósul meg. Leggyakrabban használt metódusok:**

- `onCreateView()`: a felület létrehozása, nézet visszaadása.
- `onActivityCreated()`: az Activity és Fragment közötti kapcsolat létrejötte után hívódik meg.
- `onDestroyView()`: a nézet eltávolításakor fut le.
- 
A Fragment létrehozása során a fragmentünk saját osztályát kell definiálni,
amelyek a Fragment ősosztályból örökölnek. Az Activity-hez hasonlóan a Fragmentek rendelkeznek saját életciklussal.
Saját metódusokkal is rendelkezik, mint: onCreateView(), onActivityCreated(), onDestroyView().
3 metódus felüldefiniálására van szükség ahol megtörténik a: változók és erőforrások inicializálása illetve a felhasználó felület létrehozása

### Példa
```java
public class ExampleFragment extends Fragment {
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        return inflater.inflate(R.layout.example_fragment, container, false);
    }
}
```

## Fragmentek hozzáadása és cseréje

Fragmenteket kétféleképpen lehet hozzáadni a felülethez:

### 1. Statikus módszer – XML fájlban `<fragment>` tag használata
```xml
<fragment
    android:name="com.example.ExampleFragment"
    android:id="@+id/example_fragment"
    android:layout_width="match_parent"
    android:layout_height="match_parent"/>
```

### 2. Dinamikus módszer – Java/Kotlin kódból tranzakcióval

Ehhez egy konténerre van szükség (pl. `FrameLayout`):
```xml
<FrameLayout
    android:id="@+id/container"
    android:layout_width="match_parent"
    android:layout_height="match_parent"/>
```

**Fragment hozzáadása:**
```java
FragmentTransaction tran = getSupportFragmentManager().beginTransaction();
tran.add(R.id.container, new ListFragment());
tran.commit();
```

**Fragment cseréje, visszalépés lehetőségével:**
```java
FragmentTransaction tran = getSupportFragmentManager().beginTransaction();
tran.replace(R.id.container, new DetailFragment());
tran.addToBackStack(null);
tran.commit();
```

**Visszalépés a veremben:**
```java
getSupportFragmentManager().popBackStack();
```

## Navigációs komponens (Navigation Component)

Navigation Component egy modern eszköz, ami megkönnyíti a Fragmentek közötti váltást. Korábban a Fragmentek közötti navigációt sok manuális kóddal kellett megoldani, de ez az eszköz automatizálja és leegyszerűsíti a folyamatot.
Cálja: 
- egyszerűbbé és
- biztonságosabbá tegye a Fragmentek közötti navigációt.

### Három fő része

1. **NavHostFragment- A „színpad”**
   - Egy konténer, amely megjeleníti a Fragmenteket.=
   - Ez egy konténer, ami megjeleníti a Fragmenteket. Mindig ez tartalmazza az éppen aktuális „képernyőt”.
   - Analógia: mint egy tévéképernyő, amin különböző műsorokat (Fragmenteket) tudsz nézni – de mindig csak egyet egyszerre.
   - Példa XML-ben:
     ```xml
     <fragment
         android:id="@+id/nav_host_fragment"
         android:name="androidx.navigation.fragment.NavHostFragment"
         android:layout_width="match_parent"
         android:layout_height="match_parent"
         app:navGraph="@navigation/nav_graph"
         app:defaultNavHost="true" />
     ```

2. **NavController- A „navigációs irányító”**
   - Objektum, amely vezérli a navigációt a NavHost-on belül.
   - Ez az objektum végzi el a tényleges navigációt. Ő „mondja meg” a NavHost-nak, hogy melyik Fragmentet mutassa meg.
   - Navigáció indítása:
     ```java
     NavController navController = Navigation.findNavController(activity, R.id.nav_host_fragment);
     navController.navigate(R.id.action_to_next_fragment);
     ```

3. **NavGraph (navigációs gráf)- A „navigációs térkép”**
   - XML fájl, amely deklaratívan írja le a navigációs célokat és az átmeneteket.
   - Ez egy XML fájl, ami leírja, hogy mely Fragmentek léteznek, és hogyan lehet köztük közlekedni.
   - A `res/navigation` mappában hozzuk létre.

## Navigációs gráf használata lépésről lépésre

A navigációs gráf segítségével egyszerűen tervezhető és kezelhető az alkalmazások navigációja. 
A gráfban meghatározott "destinations" fragmentek, dialogusok vagy más komponense lehetnek, 
melyek között a felhasználó navigálhat

1. **Gráf létrehozása**
   - `res/navigation/nav_graph.xml` fájlban Fragmentek és átmenetek meghatározása

2. **NavHostFragment hozzáadása a layouthoz**
   - Ez biztosítja a Fragmentek dinamikus megjelenítését

3. **Navigáció indítása NavController segítségével**
   - Fragmentből vagy Activity-ből vezérelhető

---

## Összegzés

**A Fragmentek és a Navigation Component együttes használata lehetővé teszi:**

- moduláris, újrafelhasználható felületek kialakítását,
- egyszerűbb navigációs logika megvalósítását XML-ben,
- a visszalépési lehetőségek és tranzakciók kontrollját.

Ez a kombináció különösen jól használható komplex alkalmazásoknál, ahol több képernyő logikus sorrendben történő elérésére van szükség.
