# Ohjelmistotekniikka, harjoitustyö

Harjoitustyön nimi on Probability quiz. Käyttäjä saa sarjan väitteitä, joihin vastataan antamalla todennäköisyysarvo eli reaaliluku väliltä 0-1. Kun kaikkiin väitteisiin on vastattu, käyttäjä saa [Brier-pisteytyssäännön](https://en.wikipedia.org/wiki/Brier_score) mukaisen kokonaispistetuloksen. 

## Python-versiosta

Sovelluksen on suunniteltu toimivan Python-versiolla 3.6 ja sitä korkeammilla versionumeroilla.

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/taapp/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/taapp/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

## Asennus

1. Aja seuraava komento riippuvuuksien asentamiseksi

```bash
poetry install
```

2. Käynnistä sovellus komennolla

```bash
poetry run invoke start
```
## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```


### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.


