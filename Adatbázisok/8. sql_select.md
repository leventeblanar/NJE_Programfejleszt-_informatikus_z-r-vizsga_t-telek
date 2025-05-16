<h2>Lekérdezések relációs adattáblákból – A SELECT parancs záradékainak szerepe<h2>


A SELECT parancs segítségével adatok lekérdezését végezhetjük relációs adatbázisokból. A lekérdezés záradékokból épül fel: a `SELECT` meghatározza a lekérdezett oszlopokat, a `FROM` megadja a forrástáblát, a `WHERE` szűri a sorokat. A `GROUP BY` és `HAVING` a csoportosítás és csoportfeltételek megadását teszik lehetővé, míg az `ORDER BY` a rendezést, a `LIMIT` pedig a lekérdezett sorok számának korlátozását. Ezek kombinációja teszi lehetővé a rugalmas és precíz lekérdezéseket.

## Záradék:
Az SQL-ben a záradék (angolul: clause) a SELECT utasítás egy adott részét jelenti, amely meghatározza a lekérdezés egy adott viselkedését – például, hogy milyen adatokat kérünk le, honnan, hogyan szűrünk, csoportosítunk vagy rendezünk.

- Minden záradék egy önálló funkciót lát el a lekérdezésen belül.


## 1. SELECT záradék

```sql
SELECT oszlop1, oszlop2, ...
```
- Megadja, hogy **melyik oszlopokat** kérdezzük le.
- Használható `*` a **minden oszlop** jelentésére.

**Példa:**
```sql
SELECT nev, fizetes FROM dolgozo;
```



## 2. FROM záradék

```sql
FROM tábla_neve
```
- Megadja, hogy **melyik táblából** származnak az adatok.

**Példa:**
```sql
SELECT * FROM dolgozo;
```



## 3. WHERE záradék

```sql
WHERE feltétel
```
- Szűrés feltétel alapján (csak azokat a sorokat adja vissza, amik megfelelnek).

**Példa:**
```sql
SELECT * FROM dolgozo WHERE fizetes > 300000;
```



## 4. GROUP BY záradék

```sql
GROUP BY oszlop
```
- Csoportosítás azonos értékek alapján.

**Példa:**
```sql
SELECT osztaly, AVG(fizetes) FROM dolgozo GROUP BY osztaly;
```



## 5. HAVING záradék

```sql
HAVING feltétel
```
- A `GROUP BY` után használt szűrés.

**Példa:**
```sql
SELECT osztaly, AVG(fizetes) FROM dolgozo GROUP BY osztaly HAVING AVG(fizetes) > 400000;
```



## 6. ORDER BY záradék

```sql
ORDER BY oszlop [ASC|DESC]
```
- Sorbarendezés növekvő (`ASC`) vagy csökkenő (`DESC`) sorrendben.

**Példa:**
```sql
SELECT nev, fizetes FROM dolgozo ORDER BY fizetes DESC;
```



## 7. LIMIT záradék

```sql
LIMIT szám
```
- Csak a megadott számú sort adja vissza.

**Példa:**
```sql
SELECT * FROM dolgozo LIMIT 5;
```


