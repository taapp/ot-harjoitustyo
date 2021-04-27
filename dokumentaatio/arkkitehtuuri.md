# Arkkitehtuuri

## Rakenne

![Arkkitehtuuri](./kuvat/architecture.png)

Sovelluksen kerrosarkkitehtuurin karkea esitys.

## Luokkakaavio

![Luokkakaavio](./kuvat/luokkakaavio.jpg)

Sovelluksen luokkakaavio, joka ei vastaa täysin sovelluksen nykytilaa, mutta esittää suuntaa, johon ollaan pyrkimässä.

## Päätoiminnallisuudet

### Käyttäjän sisäänkirjautuminen

Aloitusnäkymässä kun antaa käyttänimen ja salasanan, niin tapahtuu seuraavan kuvan mukainen tapahtumaketju, olettaen, että kyseinen käyttäjä on jo olemassa tietokannassa.

![Kirjautumissekvenssi](./kuvat/login_sequence.png)

### Vastauksen antaminen

Kun käyttäjä antaa vastauksen kysymykseen, tapahtuu seuraava tapahtumasarja siinä tapauksessa, että vastattu kysymys ei ole kysymyssarjan viimeinen. (Kuvassa annettu vastaus on 1.)

![Vastaussekvenssi](./kuvat/give_answer_sequence.png)