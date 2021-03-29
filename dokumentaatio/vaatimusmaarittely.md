# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksessa käyttäjät vastaavat sarjaan kysymyksiä, jotka on annettu väitteiden muodossa. Käyttäjä vastaa yksittäiseen kysymykseen antamalla todennäköisyysarvion (luku väliltä 0-1) sille, että väite pitää paikkansa. Vastattuaan sarjan kaikkiin kysymyksiin, käyttäjä saa loppuraportin, joka sisältää kokonaispistetuloksen, joka lasketaan käyttäen todennäköisyydet huomioonottavaa pisteytyssääntöä (https://en.wikipedia.org/wiki/Scoring_rule#Proper_scoring_rules), ja tilaston siitä, kuinka hyvin hänen antavat todennäköisyysarvionsa vastaavat väittämien totuusarvoihin eli kuinka hyvin todennäköisyysarviot ovat kalibroituneet (https://en.wikipedia.org/wiki/Calibrated_probability_assessment).

## Käyttäjät

Sovelluksella on käyttäjärooli normaali käyttäjä, joka voi vastata kysymyssarjaan. Lisäksi sovelluksella on suuremmilla oikeuksilla varustettu pääkäyttäjä, joka voi luoda kysymyksiä ja kysymyssarjoja.

## Toiminnallisuus

### Ennen kirjautumista

- käyttäjä voi luoda käyttäjätunnuksen sovellukseen

- käyttäjä voi kirjautua sovellukseen

### Kirjautumisen jälkeen

- käyttäjä voi vastata kysymyssarjaan

- käyttäjä nähdä viimeisimmän vastaamansa kysymyssarjan loppuraportin

- käyttäjä voi kirjautua ulos järjestelmästä

- pääkäyttäjä voi luoda uusia kysymyksiä

- pääkäyttäjä voi luoda uusia kysymyssarjoja

## Jatkokehitysideoita

- uusi kysymys ja kysymyssarjatyyppi, jossa väitteiden totuusarvoa ei vielä tiedetä (eli väitteet voivat koskea esim. tulevia tapahtumia), ja pääkäyttäjä täydentää myöhemmin totuusarvon
