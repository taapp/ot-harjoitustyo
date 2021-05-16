# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksessa käyttäjät vastaavat sarjaan kysymyksiä, jotka on annettu väitteiden muodossa. Käyttäjä vastaa yksittäiseen kysymykseen antamalla todennäköisyysarvion (reaaliluku väliltä 0-1) sille, että väite pitää paikkansa. Vastattuaan sarjan kaikkiin kysymyksiin, käyttäjä saa loppuraportin, joka sisältää kokonaispistetuloksen, joka lasketaan käyttäen todennäköisyydet huomioonottavaa pisteytyssääntöä (https://en.wikipedia.org/wiki/Scoring_rule#Proper_scoring_rules), tarkemmin sanottuna pisteyssääntöä nimeltä [Brier-pisteytys](https://en.wikipedia.org/wiki/Brier_score).

## Käyttäjät

Sovelluksella on käyttäjärooli normaali käyttäjä, joka voi vastata kysymyssarjaan. Lisäksi sovelluksella on suuremmilla oikeuksilla varustettu pääkäyttäjä, joka voi luoda kysymyssarjoja ja niihin sisältyviä kysymyksiä.

## Perusversion toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda käyttäjätunnuksen sovellukseen, jonka yhteydessä määritellään, onko uusi käyttäjätunnus pääkäyttäjä
  - Käyttäjätunnukset ovat uniikkeja
  - Käyttäjä ei voi luoda käyttäjätunnusta tai salasanaa, joka on nolla merkkiä pitkä
  - Käyttäjälle tulee näkymään huomautus, jos yritetään luoda olemassaoleva käyttäjätunnus tai jos käyttäjätunnus tai salasana on liian lyhyt

- Käyttäjä voi kirjautua sovellukseen
  - Kirjautuminen onnistuu, jos aiemmin on luotu käyttäjä, jonka käyttäjätunnus ja salasana täsmäävät syötettyihin arvoihin, ja muussa tapauksessa tulee huomautus asiasta näkymään

### Kirjautumisen jälkeen

- Tavallinen käyttäjä voi vastata valita kysymyssarjan kysymyssarjalistasta
  - Valittuaan kysymyssarjan, käyttäjä voi vastata kysymyksiin. Vastauksen täytyy olla reaaliluku lukuväliltä [0,1], muussa tapauksessa tulee huomautus asiasta näkymään.
  - Vastattuaan kysymyssarjan kaikkiin kysymyksiin, käyttäjä näkee raporttinäkymän, jossa kerrotaan vastauksista laskettu Brier-pisteytyksen mukainen pistetulos.
  - Raporttinäkymästä käyttäjä voi kirjautua ulos, mikä palauttaa näkyville sisäänkirjautumisnäkymän.

- Pääkäyttäjä näkee kirjautumisen jälkeen pääkäyttäjänäkymän, jossa pääkäyttäjä voi valita luoda uuden kysymyssarjan, vastata olemassaolevaan kysymyssarjaan tai kirjautua ulos.
  - Kysymyssarjaan vastaaminen tapahtuu pääkäyttäjällä samalla tavalla kuin tavallisella käyttäjällä.
  - Kun valitaan, että luodaan uusi kysymyssarja, tulee näkymä, jossa annetaan uuden kysymyssarjan nimi, joka täytyy olla 1-16 merkkiä pitkä. Jos näin ei ole, siitä tulee huomautus.
  - Kun kysymyssarjan nimi on annettu, voidaan luoda kysymyksiä. Kysymysluontinäkymässä voidaan luoda uusi kysymys tai lopettaa kysymysten luonti, jolloin kysymyssarja tallentuu.
  - Kysymyssarjan luomisen jälkeen palataan pääkäyttäjänäkymään.

## Jatkokehitysideoita

Jos aika riittää, seuraavia toiminnallisuuksia voidaan implementoida

- Loppuraportissa näytetään pisteytyksen lisäksi tietoa vastausten kalibraatiosta.

- Annetut vastaukset tallentuvat ja aikaisempia loppuraportteja voi tarkastella.

- Uusi kysymystyyppi (ennuste) ja kysymyssarjatyyppi (ennustesarja tai ennustekilpailu), jossa väitteiden totuusarvoa ei vielä tiedetä (eli väitteet voivat koskea esim. tulevia tapahtumia), ja pääkäyttäjä täydentää myöhemmin totuusarvon

- Käyttäjä voi tarkastella koko vastaushistoriaansa.

- Pääkäyttäjä voi tarkastella tilastoja siitä, miten yksittäisiin kysymyksiin on vastattu.

- Kysymyssarjalle voidaan nähdä ranking-lista niistä käyttäjistä, jotka ovat saaneet parhaat pisteet.

- Useiden eri pisteytyssääntöjen implementointi, ja kysymyssarjaa luotaessa määritetään, mitä pisteytyssääntöä käytetään.