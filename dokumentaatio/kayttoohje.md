# Käyttöohje

## Sovelluksen käynnistäminen

1. Aja seuraava komento riippuvuuksien asentamiseksi

```bash
poetry install
```

2. Alusta sovelluksen käyttämä tietokanta komennolla

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla

```bash
poetry run invoke start
```

Huom. Siinä tapauksessa, että testaukseen ja testikattavuuteen liittyviä komentoja on ajettu, niin silloin build-komento tulee suorittaa ennen start-komentoa.

## Kirjautuminen

Kun sovellus käynnistyy, nähdään ensimmäisenä kirjautumisnäkymä. Kirjautumisnäkymässä voidaan luoda uusi käyttäjä tai kirjautua sisään. Kummassakin tapauksessa syötteenä käytetään Username ja Password kenttiä, joihin laitetaan käyttäjätunnus ja salasana. Lisäksi käyttäjää luodessa valitaan määritetään Admin-valinnalla, onko uusi käyttäjä pääkäyttäjä (tumma ruutu) tai tavallinen käyttäjä (valkea ruutu). Oletuksena käyttäjä on tavallinen käyttäjä.

Kun käyttäjää luodaan niin käyttäjänimi ja salasana eivät saa olla nolla merkkiä pitkiä. Lisäksi käyttäjätunnusten tulee olla uniikkeja. Jos näitä ehtoja yrittää rikkoa, niin silloin tulee huomautus näkymään.

Kun kirjaudutaan sisään, tulee käyttäjänimen ja salasanan vastata luotujen käyttäjien tietoja. Jos näin ei ole, tulee huomautus näkymään.

## Kysymyssarjan valitseminen ja kysymyksiin vastaaminen

Kun tavallinen käyttäjä onnistuu kirjautumaan, hän tulee näkymään, jossa hän voi valita kysymyssarjan. Kun käyttäjä valitsee kysymyssarjan, tulee uusi näkymä, jossa näkyy kysymyssarjan ensimmäinen kysymys (olettaen, että kysymyssarjassa on enemmän kuin nolla kysymystä). Kysymykseen vastataan syöttämällä reaaliluku lukuväliltä [0,1]. Jos annettu syöte ei vastaa tätä, siitä tulee huomautus. 

Kun kaikkiin kysymyksiin on vastattu, tulee raporttinäkymä, jossa esitetään vastauksien perusteella laskettu Brier-pisteytyksen mukainen pistetulos. Brier-pisteet toimivat siten, että mitä pienempi luku on, sitä parempi, mutta 0 on minimi eli täydellinen tulos. Raporttinäkymästä voi kirjautua ulos, jolloin palataan kirjautumisnäkymään

## Pääkäyttäjän toiminnallisuus: kysymyssarjan luominen

Kun pääkäyttäjä kirjautuu sisään, tulee pääkäyttäjänäkymä, jossa voi valita joko luoda uuden kysymyssarjan, vastata olemassaolevaan kysymyssarjaan, tai kirjautua ulos. Kysymyssarjaan vastaaminen toimii samalla tavalla pääkäyttäjälle kuin tavalliselle käyttäjälle. 

Jos valitaan luoda uusi kysymyssarja, tulee näkymä, jossa syötetään uuden kysymyssarjan nimi, joka täytyy olla 1-16 merkkiä pitkä. Jos näin ei ole, siitä tulee huomautus näkymään. Kun kysymyssarjan nimi on annettu, siirrytään kysymysluontinäkymään. Kysymysluontinäkymässä voi määrittää uuden kysymyksen tai lopettaa kysymysten luonnin. 

Kohtaan "statement" syötetään kysymyksen väite. Kohtaan "check if true" syötetään, onko väite tosi (tumma ruutu vastaa väitettä, joka on totta, ja valkoinen ruutu väitettä, joka ei ole totta). Kohtaan "comment" voi syöttää kommentin, joka on kysymykseen liittyvää lisätietoa (esimerkiksi lähdeviite).

Kun valitaan lopettaa kysymysten luonti, kysymyssarja ja kysymykset tallentuvat ja palataan pääkäyttäjänäkymään. 