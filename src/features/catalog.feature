#noinspection CucumberUndefinedStep

Feature: F-001 Lista över aktuella böcker att läsa

  Scenario: Visa startvyn Läslistan
    Given jag surfar till Läslistan
    Then ska information om Katalog visas
    And knappen Katalog ska vara inaktiv

  Scenario: Favoritmarkera en bok
    Given jag surfar till Läslistan
    When jag favoritmarkerar boken "Ormar på ett plan: En Python-berättelse"
    Then boken "Ormar på ett plan: En Python-berättelse" ska vara favoritmarkerad
    # todo även kolla att den återfinns som min bok?




