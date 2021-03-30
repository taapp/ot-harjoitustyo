# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksessa käyttäjät vastaavat sarjaan kysymyksiä, jotka on annettu väitteiden muodossa. Käyttäjä vastaa yksittäiseen kysymykseen antamalla todennäköisyysarvion (reaaliluku väliltä 0-1) sille, että väite pitää paikkansa. Vastattuaan sarjan kaikkiin kysymyksiin, käyttäjä saa loppuraportin, joka sisältää kokonaispistetuloksen, joka lasketaan käyttäen todennäköisyydet huomioonottavaa pisteytyssääntöä (https://en.wikipedia.org/wiki/Scoring_rule#Proper_scoring_rules), ja tilaston siitä, kuinka hyvin todennäköisyysarviot vastaavat väittämien totuusarvoja eli kuinka hyvin todennäköisyysarviot ovat kalibroituneet (https://en.wikipedia.org/wiki/Calibrated_probability_assessment).

## Käyttäjät

Sovelluksella on käyttäjärooli normaali käyttäjä, joka voi vastata kysymyssarjaan. Lisäksi sovelluksella on suuremmilla oikeuksilla varustettu pääkäyttäjä, joka voi luoda kysymyksiä ja kysymyssarjoja.

## Toiminnallisuus

### Ennen kirjautumista

- käyttäjä voi luoda käyttäjätunnuksen sovellukseen
  - käyttäjätunnukset ovat uniikkeja

- käyttäjä voi kirjautua sovellukseen

### Kirjautumisen jälkeen

- käyttäjä voi vastata kysymyssarjaan

- käyttäjä voi nähdä viimeisimmän vastaamansa kysymyssarjan loppuraportin

- käyttäjä voi kirjautua ulos järjestelmästä

- pääkäyttäjä voi luoda uusia kysymyksiä

- pääkäyttäjä voi luoda uusia kysymyssarjoja

## Jatkokehitysideoita

Jos aika riittää, seuraavia toiminnallisuuksia voidaan implementoida

- uusi kysymystyyppi (ennuste) ja kysymyssarjatyyppi (ennustesarja tai ennustekilpailu), jossa väitteiden totuusarvoa ei vielä tiedetä (eli väitteet voivat koskea esim. tulevia tapahtumia), ja pääkäyttäjä täydentää myöhemmin totuusarvon

- käyttäjä voi tarkastella koko vastaushistoriaansa

- pääkäyttäjä voi tarkastella tilastoja siitä, miten yksittäisiin kysymyksiin on vastattu

- kysymyssarjalle voidaan nähdä ranking-lista niistä käyttäjistä, jotka ovat saaneet parhaat pisteet

- useiden eri pisteytyssääntöjen implementointi, ja kysymyssarjaa luotaessa määritetään, mitä pisteytyssääntöä käytetään