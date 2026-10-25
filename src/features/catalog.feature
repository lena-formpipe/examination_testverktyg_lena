# US01 Som en användare vill jag
# se en katalog med lista över böcker
# så att jag vet vilka böcker jag kan välja från
#
# US02 Som en användare vill jag
# kunna favoritmarkera en bok i katalogen
# så att jag enkelt ser vilka böcker som intresserar mig.
#
# US03 Som en användare vill jag
# kunna avmarkera en favoritmarkerad bok i katalogen
# så att jag kan ta bort böcker när mitt intresse förändras.
#
# US06 Som en användare vill jag
# kunna navigera till de olika funktionerna
# så att jag kan nå den den funktion jag behöver
#noinspection CucumberUndefinedStep

Feature: Kunna se katalog över aktuella böcker och favoritmarkera dessa

  Scenario: Visa startvyn Läslistan
    Given jag surfar till Läslistan
    Then ska information visas om boken Ormar på ett plan: En Python-berättelse
    And knappen Katalog ska vara inaktiv


  Scenario: Favoritmarkera en bok
    Given jag surfar till Läslistan
    When jag favoritmarkerar boken "Ormar på ett plan: En Python-berättelse"
    Then boken "Ormar på ett plan: En Python-berättelse" ska vara favoritmarkerad
    And boken "Ormar på ett plan: En Python-berättelse" ska finnas på sidan Mina böcker


  Scenario: Avmarkera en favoritmarkerad bok
    Given jag surfar till Läslistan
    When jag favoritmarkerar boken "Ormar på ett plan: En Python-berättelse"
    And jag avmarkerar boken "Ormar på ett plan: En Python-berättelse"
    Then ska boken "Ormar på ett plan: En Python-berättelse" inte vara favoritmarkerad





