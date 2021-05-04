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