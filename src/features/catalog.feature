#noinspection CucumberUndefinedStep

Feature: F-001 Lista över aktuella böcker att läsa

  Scenario: Favoritmarkera en bok
    Given jag surfar till Läslistan
    When jag favoritmarkerar boken "Ormar på ett plan: En Python-berättelse"
    Then boken "Ormar på ett plan: En Python-berättelse" ska vara favoritmarkerad




