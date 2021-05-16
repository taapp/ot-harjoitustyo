# Ohjelmistotekniikka, harjoitustyö

Harjoitustyön nimi on Probability quiz. Käyttäjä saa sarjan väitteitä, joihin vastataan antamalla todennäköisyysarvo eli reaaliluku väliltä 0-1. Kun kaikkiin väitteisiin on vastattu, käyttäjä saa [Brier-pisteytyssäännön](https://en.wikipedia.org/wiki/Brier_score) mukaisen kokonaispistetuloksen. 

## Python-versiosta

Sovelluksen on suunniteltu toimivan Python-versiolla 3.6 ja sitä korkeammilla versionumeroilla.

## Dokumentaatio

[Käyttöohje](https://github.com/taapp/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/taapp/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuurikuvaus](https://github.com/taapp/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Testausdokumentti](https://github.com/taapp/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)

[Työaikakirjanpito](https://github.com/taapp/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

## Releaset

[Viikon 5 release](https://github.com/taapp/ot-harjoitustyo/releases/tag/viikko5)

[Viikon 6 release](https://github.com/taapp/ot-harjoitustyo/releases/tag/viikko6)

## Asennus

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
## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

Huom. Siinä tapauksessa, että testaukseen ja testikattavuuteen liittyviä komentoja on ajettu, niin silloin build-komento tulee suorittaa ennen start-komentoa.

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

### Pylint

Koodin laatutarkastuksen voi suorittaa komennolla

```bash
poetry run invoke lint
```