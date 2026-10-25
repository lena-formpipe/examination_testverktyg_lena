# US07 Som en användare vill jag
# kunna se statistik över böcker och mina favoriter
# så att jag har kunskap om systemets statistik.
#
# US06 Som en användare vill jag
# kunna navigera till de olika funktionerna
# så att jag kan nå den den funktion jag behöver
# noinspection CucumberUndefinedStep


Feature: Visa vyn Statistik

  Scenario: Visa vyn Statistik
    Given   jag surfar till Läslistan
    When    jag klickar på knappen statistik
    Then    ska information om statistik visas
    And     ska statistik om favoritmarkeringar visas
    And     ska knappen statistik ska vara inaktiv
