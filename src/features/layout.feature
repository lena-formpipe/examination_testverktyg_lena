#noinspection CucumberUndefinedStep

Feature: F-006 Kunna välja rätt vy
"""
  Scenario: Visa vyn Mina böcker med tom lista
    Given jag surfar till Läslistan
    When jag klickar på knappen Mina böcker
    Then ska information om Mina böcker visa tom lista
    And knappen Mina böcker ska vara inaktiv
"""

  Scenario: Visa vyn Statistik
    Given jag surfar till Läslistan
    When jag klickar på knappen Statistik
    Then ska information om Statistik visas
    And knappen Statistik ska vara inaktiv

  Scenario: Visa vyn Lägg till bok
    Given jag surfar till Läslistan
    When jag klickar på knappen Lägg till bok
    Then ska information om att lägga till bok visas
    And knappen Lägg till bok ska vara inaktiv

  Scenario: Visa startvyn Läslistan
    Given jag surfar till Läslistan
    Then ska information om Katalog visas
    And knappen Katalog ska vara inaktiv

