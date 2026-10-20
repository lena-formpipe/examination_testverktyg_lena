#noinspection CucumberUndefinedStep

Feature: Visa vyn Mina böcker

  Scenario: Visa vyn Mina böcker med tom lista
    Given jag surfar till Läslistan
    When jag klickar på knappen Mina böcker
    Then ska information om Mina böcker visa tom lista
    And knappen Mina böcker ska vara inaktiv


