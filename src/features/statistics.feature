#noinspection CucumberUndefinedStep

Feature: Visa vyn Mina Statistik

  Scenario: Visa vyn Statistik utan favoritmarkerade böcker
    Given   jag surfar till Läslistan
    When    jag klickar på knappen statistik
    Then    ska information om statistik visas
    And     ska statistik om favoritmarkeringar visa 0
    And     ska knappen statistik ska vara inaktiv
